import pandas as pd
import csv
import os
from datetime import datetime, timedelta


def copy_from_log_file(config):
    folder = config['SETTINGS']['folderExecution']
    log_file = open(config['SETTINGS']['logFile'],'r')
    results_file = open(folder+r'\failedSubscriptions.txt','w')
    line = log_file.readline()
    while(line):
        if(line.find("FAILED SUBSCRIPTION") != -1):
            results_file.write(line)
        line = log_file.readline()
    results_file.close()


def import_data(config):
    # Just a few settings
    pd.set_option('max_colwidth', 100)
    # Set the file where we are going to read from
    folder = config['SETTINGS']['folderExecution']
    historical_log_path = config['SETTINGS']['historyFailedSubsFile']
    historical_log = open(historical_log_path, "a+")
    dr = pd.read_fwf(folder+r'\failedSubscriptions.txt',widths=[10,19,1500], header=None)
    dr.columns = ['date','time','data']
    # Define new dataframe that finally will be written to the final file output
    df = pd.DataFrame(columns=['statement'])
    for index, row in dr.iterrows():
        start = row['data'].find("FAILED SUBSCRIPTION")+21
        end = row['data'].find("': Error Msg: ")
        dateandtime = datetime.strptime(row['date'] +" "+ row['time'][:-10] , "%Y-%m-%d %H:%M:%S")
        one_hour_ago = datetime.now() - timedelta(minutes=60)
        name_subscription = row['data'][start:end]
        # If the failed subscription failed more than an hour ago, it won't be considered
        if(dateandtime >= one_hour_ago):
            statement = 'TRIGGER SUBSCRIPTION \"' + name_subscription +'\" FOR PROJECT \"PROJECT NAME\";'
            df.loc[index] = statement
            historical_log.write(name_subscription + " ---------###----------- " + str(dateandtime)+"\n")
    # Remove the duplicates
    dtt = df.drop_duplicates()
    dtt.to_csv(folder+r"\toexecute.txt",index=False,header=False,quoting=csv.QUOTE_NONE)


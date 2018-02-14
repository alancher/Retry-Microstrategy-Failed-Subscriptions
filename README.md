# Retry-Microstrategy-Failed-Subscriptions

## Goal
The goal is to retry Microstrategy subscriptions that have failed. The script was written on Python 3.6

## How to use it

Make a bat or sh that has:
python Main.py

Then schedule the bat/sh every hour. The script will check on the Microstrategy log file dsserrors.log the subscriptions that failed in the last hour and try to rerun them 

## Parameters to change

* All the ini file

* In line 38 of FileManager.py change the project name
 
* executeCommands.bat parameters

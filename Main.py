import FileManager as fm
from subprocess import Popen
import configparser


def initialize_configs():
    config = configparser.ConfigParser()
    config.read('configFile.ini')
    return config


def execute_commands(config):
    p = Popen(config['SETTINGS']['batFile'], cwd=config['SETTINGS']['folderExecution'])
    stdout, stderr = p.communicate()


config = initialize_configs()
fm.copy_from_log_file(config)
fm.import_data(config)
execute_commands(config)
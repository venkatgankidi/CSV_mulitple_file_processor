

import logging
from datetime import date
from ConfigProvider import *


class Logger():
    def __init__(self):
        pass

    @staticmethod
    def __get_log__():
        config = ConfigProvider.__config_properties__()
        log_dir = config.get('log','log_dir')
        log_format = config.get('log','format')
        log_file_name="log_"+str(date.today())+".log"
        logging.basicConfig(filename=log_dir+'/'+log_file_name, level=logging.DEBUG, format=log_format)
        return logging


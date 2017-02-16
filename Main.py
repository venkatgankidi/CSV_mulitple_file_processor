
from FileProcessor import *

import os
from Logger import *
from ConfigProvider import *


def main():
    file_processor=FileProcessor()
    log = Logger().__get_log__()
    config = ConfigProvider.__config_properties__()
    input_dir = config.get('config','input_dir')
    ready_to_process_dir = config.get('config','ready_to_process_dir')
    error_report_dir = config.get('config','error_report_dir')
    rejected_files_dir = config.get('config','rejected_files_dir')
    files = os.listdir(input_dir)
    log.info("started_processing")
    for f in files:
        input_file=input_dir+'/'+f
        pass_dst = ready_to_process_dir+'/'+f
        err_dst = rejected_files_dir+'/'+f
        log.info("started processing file "+ f)
        failed=file_processor.process_file(input_file,error_report_dir,f)
        if failed:
            os.rename(input_file,err_dst)
            log.info(f+" file moved to rejected directory")
        else:
            os.rename(input_file,pass_dst)
            log.info(f + " file moved to ready to process directory")
        log.info("completed processing file "+f)


if __name__ == "__main__":
    main()

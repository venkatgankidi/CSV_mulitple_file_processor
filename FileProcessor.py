from Validator import *
import csv
from Mail import *


class FileProcessor():

    def __init__(self):
        self.log = Logger().__get_log__()

    def process_file(self,inputfile,outputdir,filename):
        rename=str(filename).replace('.csv','.txt')
        output_file=outputdir+"/"+rename
        failed=True
        csv_file = open(inputfile,'r')
        csv_file1 = open(inputfile,'r')
        input_file = csv.reader(csv_file, delimiter=',')
        input_file1 = csv.reader(csv_file1, delimiter=',')
        validator = Validator()
        header_problems= validator.header_validator(input_file1)
        value = len(header_problems)
        self.log.info("header validation completed with "+str(value)+" problems")
        if value != 0:
            write_problems(header_problems,open(output_file,'w'))
            Mail().send_mail(rename, output_file)
            return failed
        else:
            data_problems = validator.data_validator(input_file)
            value = len(data_problems)
            self.log.info("data validation completed with "+str(value)+" problems")
            if value != 0:
                write_problems(data_problems, open(output_file, 'w'))
                Mail().send_mail(rename, output_file)
                return failed

        return False





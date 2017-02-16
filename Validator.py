
import json
from csvvalidator import *
from Logger import *
from ConfigProvider import *


class Validator:
    def __init__(self):
        self.json_Data = ConfigProvider.__json_config__()
        self.error_code = self.json_Data["error_code_mapping"]
        self.error_message=self.json_Data["error_message_mapping"]
        self.headers=self.json_Data["headers"]
        self.log = Logger().__get_log__()

    def header_validator(self,input_file):
        self.log.info("starting header validation")
        validator = CSVValidator(self.headers)
        validator.add_header_check(self.error_code['error1'],self.error_message['error1'])
        validator.add_record_length_check(self.error_code['error2'],self.error_message['error2'])
        problems=validator.validate(input_file)
        return problems

    def data_validator(self,input_file):
        self.log.info("starting data validation")
        validator = CSVValidator(self.headers)
        int_list = []
        str_list = []

        for column in self.json_Data["header_mapping"]:
            column_name = self.json_Data["header_mapping"][column]
            column_type = self.json_Data["value_mapping"][column]

            if column_type == "String":
                validator.add_value_check(column_name, str, self.error_code['error3'],column_name + self.error_message['error3'])
            elif column_type == "Date":
                validator.add_value_check(column_name, datetime_string('%Y%m%d'), self.error_code['error4'],
                                          column_name + self.error_message['error4'])
            elif column_type == "IntorNull":
                int_list.append(column_name)
            elif column_type == "Stringnotnull":
                str_list.append(column_name)

        def custom_int_check(r):
            valid = False
            for l in int_list:
                if r[l] is '':
                    valid = True
                else:
                    try:
                        value = int(r[l])
                        valid = type(value) == int
                    except ValueError:
                        valid = False
                if not valid:
                    raise RecordError(self.error_code['error5'], l + self.error_message['error5'])

        def custom_string_check(r):
            valid = True
            for s in str_list:
                if r[s] is '':
                    valid = False
                if not valid:
                    raise RecordError(self.error_code['error6'], s + self.error_message['error6'])

        validator.add_record_check(custom_int_check)
        validator.add_record_check(custom_string_check)
        problems = validator.validate(input_file)
        return problems








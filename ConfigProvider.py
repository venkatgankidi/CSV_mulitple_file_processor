

import json
import ConfigParser


class ConfigProvider:
    def __init__(self):
        pass

    @staticmethod
    def __json_config__():
        json_file = open("config/config.json")
        json_data = json.load(json_file)
        return json_data

    @staticmethod
    def __config_properties__():
        config = ConfigParser.RawConfigParser()
        config.read('config/config.properties')
        return config

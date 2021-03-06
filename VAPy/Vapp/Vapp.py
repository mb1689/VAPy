import getpass

try:
    import ujson as json
except:
    import json

import VAPy

class Vapp(object):
    

    def __init__(self):

        #attributes to be populated from config.json
        self.app_name = ""        
        self.app_dir = "./"
        self.nsfw = False
        self.subverses = []
        self.target_content = []

        self.load_config()
        if not self.validate_config_load():
            print("There is a problem with config.json")
            return None

        self.vapy = VAPy.VAPy()
        pwd = getpass.getpass(prompt="Enter password: ")
        self.vapy.load_profile(self.profile, pwd)
        



    def load_config(self):
        with open('./Vapp/config.json') as f:
            config = json.load(f)
        for key in config.keys():
            setattr(self, key, self.parse_config_string(config[key]))


    def parse_config_string(self, string):
        if type(string) != str:
            return string
        if string == "True":
            return True
        elif string == "False":
            return False
        elif string == "None":
            return None
        elif string.endswith(".json"):
            with open(string) as f:
                return json.load(f) 
        else:
            return string

    def validate_config_load(self):
        return True if (
                       type(self.app_name) == str and len(self.app_name) > 0 and
                       len(self.subverses) > 0
                       ) else False




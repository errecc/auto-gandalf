import requests
import ollama
import pymongo
from string import Template
import yaml
from pprint import pprint
import datetime



class ConfigLoader:
    def __init__(self):
        """Loads """
        with open("config.yaml", 'r') as fp:
            self.config = yaml.safe_load(fp)
        self.global_delay = self.config["global_delay"]
        self.mongo_host = self.config["mongodb_host"]
        self.mongo_port = self.config["mongodb_port"]
        self.db_name = self.config["db_name"]

    def show(self):
        print("Config loaded:")
        pprint(self.config)
        print("\n"*2)


class DefenderGrabber:
    def __init__(self):
        self.session = requests.Session()

    def grab_defenders(self):
        """
        Attemps to query a question to gandalf with an uninvalid defender to
        retrieve all possible defenders and store them in a database
        """
        raise NotImplementedError


class PasswordGrabber:
    def __init__(self, answer):
        raise NotImplementedError

    def grab_password(self):
        raise NotImplementedError


class AdversarialPayloadGenerator:
    def __init__(self, model):
        raise NotImplementedError

    def generate_payload(self, model):
        raise NotImplementedError


class GandalfAdversary:
    def __init__(self, defender):
        raise NotImplementedError



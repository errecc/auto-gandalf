import requests
import ollama
import pymongo


class CookieGrabber:
    def __init__(self):
        raise NotImplementedError

    def grab_cookies(self):
        raise NotImplementedError


class DefenderGrabber:
    def __init__(self):
        raise NotImplementedError

    def grab_defenders(self):
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

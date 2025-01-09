"""Evaluates the results of prompting to Gandalf"""
import pandas as pd
import torch


class PasswordGrabber:
    def __init__(self, answer):
        self.answer = answer

    def grab_password(self):
        """
        Process an answer from Gandalf and grab the password if it is in the
        answer, else, return False
        """
        raise NotImplementedError


class AutoGandalfDatabaseLoader:
    def __init__(self):
        self.X = None
        self.Y = None


"""Evaluates the results of prompting to Gandalf"""
import pandas as pd
import torch



class AutoGandalfDatabaseLoader:
    def __init__(self):
        self.X = None
        self.Y = None


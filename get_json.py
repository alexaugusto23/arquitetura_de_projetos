import requests
import json
import time
from unittest import TestCase, main

class Blog:
    def __init__(self, nome):
        self.nome = nome 


    def posts(self):
        endereco = "www.google.com"
        response = requests.get(endereco)
        return response.json()

    def __repr__(self):
        pass
#!/usr/bin/python3
'''
    json module
'''


import json


def load_from_json_file(filename):
    '''
        json function
    '''
    with open(filename, "r", encoding="utf-8") as datafile:
        return json.load(datafile)

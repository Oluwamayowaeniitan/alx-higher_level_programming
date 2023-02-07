#!/usr/bin/python3
'''
    json module
'''


import json


def save_to_json_file(my_obj, filename):
    '''
        json function
    '''
    filename = json.dump(my_obj)
    return filename

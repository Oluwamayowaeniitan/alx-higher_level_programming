#!/usr/bin/python3
'''
    json module
'''


import json


def save_to_json_file(my_obj, filename):
    '''
        json function
    '''
    with open(filename, mode="w") as filetemp:
        filetemp.write(json.dumps(my_obj))

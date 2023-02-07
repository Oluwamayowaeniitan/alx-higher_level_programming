#!/usr/bin/python3
'''
    module to append
'''


def append_write(filename="", text=""):
    '''
        write an input
    '''

    with open(filename, "a", encoding="utf-8") as filetemp:
        return filetemp.write(text)

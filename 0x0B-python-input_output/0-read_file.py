#!/usr/bin/python3
def read_file(filename=""):
    with open("filename", "r", encoding="utf-8") as filetemp:
        read_data = filetemp.read()
    print(read_data, end="")

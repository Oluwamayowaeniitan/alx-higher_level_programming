#!/usr/bin/python3
def read_file(filename=""):
    with open("UTF8.txt", encoding="UTF-8") as filename:
        print(filename.read())

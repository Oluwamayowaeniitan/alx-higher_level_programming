#!/usr/bin/python3
def best_score(a_dictionary):
    new = {}
    for (k, v) in a_dictionary:
        new[k] = max(v)
        return new

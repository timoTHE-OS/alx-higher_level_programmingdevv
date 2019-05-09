#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return "None"
    max = list(a_dictionary.values())[0]
    for k in a_dictionary:
        if a_dictionary[k] > max:
            max = a_dictionary[k]
            key = k
    return key

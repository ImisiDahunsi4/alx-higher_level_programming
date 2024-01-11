#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary
    for key in newdic:
        value = newdic[key]
        newdic[key] = value * 2
    return newdic

#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set()
    for element in my_list:
        uniq_int.add(element)
    result = sum(uniq_int)
    return result

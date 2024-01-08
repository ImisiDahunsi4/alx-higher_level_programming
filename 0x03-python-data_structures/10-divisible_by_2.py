#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lenght = len(my_list)
    newlist = []
    for i in range(lenght):
        if my_list[i] % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist

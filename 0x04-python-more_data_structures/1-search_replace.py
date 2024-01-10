#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        # create new list
        new_list = []
        # iterate through the list through a var
        for element in my_list:
            new_element = replace if element == search else element
            new_list.append(new_element)
        return new_list

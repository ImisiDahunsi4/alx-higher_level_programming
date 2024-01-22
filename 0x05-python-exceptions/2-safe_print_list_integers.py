#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printedElements = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]))
                printedElements += 1
    except (TypeError, ValueError):
        pass
    print()
    return printedElements

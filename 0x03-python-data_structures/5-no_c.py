#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        newsrt = my_string.translate({ord("c"): None})
        secsrt = newsrt.translate({ord("C"): None})
        return secsrt
    return my_string

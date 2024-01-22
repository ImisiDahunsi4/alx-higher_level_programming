#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Result = a / b
    except:
        print("Inside result: {}".format(None))
        return None
    else:
        print("Inside result: {}".format(Result))
        return Result

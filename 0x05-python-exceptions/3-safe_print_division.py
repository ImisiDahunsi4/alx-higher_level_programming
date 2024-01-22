#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except Exception as e:
        result = None
    finally:
        print("Invalid result: {}".format(result))
        return result

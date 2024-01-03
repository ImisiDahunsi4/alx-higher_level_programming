#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
number_rem = number % 10

if number_rem > 5:
    print(f"Last digit of {number} is {number_rem} and is greater than 5")
elif number_rem == 0:
    print(f"Last digit of {number} is {number_rem} and is 0")
elif 0 != number_rem < 6:
    print(
        f"Last digit of {number} is {number_rem} "
        f"and is less than 6 and not 0"
    )
    print(f"Last digit of {number} is {number_rem} and is less than 6 and not 0")

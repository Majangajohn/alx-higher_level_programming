#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5 and number > 0:
    print("Last digit of {0} is {1}".format(number, last_digit), end="")
    print(" and is greater than 5")
elif last_digit == 0 and number > 0:
    print("Last digit of {0} is {1} and is 0".format(number, last_digit))
elif last_digit >0 and last_digit < 6 and number > 0:
    print("Last digit of {0} is {1}".format(number, last_digit), end="")
    print(" and is less than 6 and not 0")
else:
    print("Last digit of {0} is {1}".format(number, (-1 * last_digit)), end="")
    print(" and is less than 6 and not 0")

#!/usr/bin/python3
""" 
Prints each integer from the list 'my_list' on a new line.
    Uses str.format() to format and print the integers.
    
Parameters:
my_list (list): A list of integers to be printed.
"""

def print_list_integer(my_list=[]):

    for numbers in my_list:
        print("{:d}".format(numbers), end="\n")

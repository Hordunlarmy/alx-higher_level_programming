#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # a function that prints all integers of a list, in reverse order.

    if (my_list):
        for num in reversed(my_list):
            print("{:d}".format(num))

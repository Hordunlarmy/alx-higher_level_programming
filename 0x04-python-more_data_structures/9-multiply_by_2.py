#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # a function that returns a new
    # dictionary with all values multiplied by 2

    new_dict = {}
    for k, value in a_dictionary.items():
        new_dict[k] = value * 2
    return (new_dict)

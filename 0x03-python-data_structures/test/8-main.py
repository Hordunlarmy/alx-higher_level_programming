#!/usr/bin/python3
def max_integer(my_list=[]):
    # a function that finds the biggest integer of a list.

    if (my_list == []):
        return (None)
    else:
        my_list.sort()
        max_element = my_list[-1]
        return (max_element)

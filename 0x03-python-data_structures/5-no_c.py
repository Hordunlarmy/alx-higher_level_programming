#!/usr/bin/python3
def no_c(my_string):
    # A function that removes all characters 'c' and 'C' from a string.

    char_list = list(my_string)
    char_list = [char for char in char_list if char.lower() != 'c']
    my_string = ''.join(char_list)

    return my_string

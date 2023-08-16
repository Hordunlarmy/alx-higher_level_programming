#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # a function that deletes keys with
    # a specific value in a dictionary.

    del_keys = []
    for key in a_dictionary:
        if (a_dictionary[key] == value):
            del_keys.append(key)
    for key in del_keys:
        del a_dictionary[key]
    return (a_dictionary)

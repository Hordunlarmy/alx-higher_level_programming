#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # A function that prints the first x elements of a list and only integers.

    index = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            index += 1
        except (TypeError, ValueError):
            continue
    print()
    return (index)

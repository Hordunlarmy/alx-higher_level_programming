#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    #  a function that prints x elements of a list

    index = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            index = index + 1
        except IndexError:
            break
        print("")
    return (index)

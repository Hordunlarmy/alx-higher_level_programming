#!/usr/bin/python3
def weight_average(my_list=[]):
    # a function that returns the weighted
    # average of all integers tuple (<score>, <weight>)

    if (my_list) and (len(my_list) > 0):
        num, denom = 0, 0
        for tp in my_list:
            num += (tp[0] * tp[1])
            denom += tp[1]
        return (num / denom)
    return (0)

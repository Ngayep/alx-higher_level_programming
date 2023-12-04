#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    Max_value = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > Max_value:
            Max_value = my_list[i]

    return Max_value

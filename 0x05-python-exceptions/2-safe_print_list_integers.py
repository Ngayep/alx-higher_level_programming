#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    index = 0
    while index < x:
        try:
            element = my_list[index]
            print("{:d}".format(element), end="")
        except (IndexError, TypeError, ValueError):
            break
        index += 1

    print()

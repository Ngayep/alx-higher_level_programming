#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    index = 0
    printed_count = 0

    while printed_count < x:

        try:
            element = my_list[index]
            if type(element) in (int, long):
                print("{:d}".format(element), end="")
                printed_count += 1
        except (IndexError, TypeError):
            pass
        index += 1

    print()
    return printed_count

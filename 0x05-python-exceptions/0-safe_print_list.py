#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    printed_count = 0
    index = 0

    while printed_count < x:
        try:
            element = my_list[index]
            print(element, end = "")
            printed_count += 1
        except IndexError:
            break
        index += 1
        print()
        return printed_count


#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a subclass of list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        """prints the sorted list"""
        print(sorted_list)

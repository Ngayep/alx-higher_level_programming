#!/usr/bin/python3
"""Class that contains the Mylist class"""


class MyList(list):
    """class inheriting from list"""
    def print_sorted(self):
        """method that prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)

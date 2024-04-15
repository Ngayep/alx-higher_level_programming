#!/usr/bin/python3
class MyList(list):
    """class inheriting from list"""
    def __init__(self):
        """initializing the MYlist class"""
        super().__init__()

    def print_sorted(self):
        """method that prints a sorted list"""
        print(sorted(self))

#!/usr/bin/python
class Mylist(list):
    """
    custom class that inherits from th build in list class

    public instance method: print the list in ascending order
    """

    def print_sorted(self):
        """
        prints the list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)

#!/usr/bin/python3
class MyList(list):
    """
    custom class that inherits from th build in list class

    public instance method: print the list in ascending order
    """

    def print_sorted(self):
        """
        prints the list in ascending order
        """
        print(sorted(self))

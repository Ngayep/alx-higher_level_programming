#!/usr/bin/python3
"""a class with a method that raises an exception"""


class BaseGeometry:
    """method that raises an exception with the message not implemented"""
    def area(self):
        """method still to be implemented"""
        raise Exception("area() is not implemented")

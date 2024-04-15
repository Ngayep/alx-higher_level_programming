#!/usr/bin/python3
"""defines a Rectangle class"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle

        Args:
            width (int): the width of the rectangle
            height (int) : the height of the rectangle
        """

        self.width = width
        self.height = height

    def width(self):
        """retrieves width attribute"""
        return self.__width

    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """sets the height of the rectangle"""
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

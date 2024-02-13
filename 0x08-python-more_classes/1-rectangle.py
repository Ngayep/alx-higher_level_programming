#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

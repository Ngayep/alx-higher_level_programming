#!/usr/bin/python3
"""module import for a child of BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a child of BaseGeometry class"""

    def __init__(self, width, height):
        """instantiation method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        """area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """special method that returns the printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

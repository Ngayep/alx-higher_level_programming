#!/usr/bin/python3
"""imported module for a child of BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a child of BaseGeometry class"""

    def __init__(self, width, height):
        """"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

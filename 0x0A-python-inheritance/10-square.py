#!/usr/bin/python3
"""module import for a child of BaseGeometry class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """a child of BaseGeometry class"""

    def __init__(self, size):
        """instantiation method"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """returns a string with the area"""
        return super().area()

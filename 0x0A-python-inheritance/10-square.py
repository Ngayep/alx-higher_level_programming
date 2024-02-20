#!/usr/bin/python3
"""module import for a child of BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """a child of BaseGeometry class"""

    def __init__(self, size):
        """instantiation method"""

        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
        self.__size = size

    def area(self):
        """returns a string with the area"""
        return super().area()

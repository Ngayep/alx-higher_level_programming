#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """a child of BaseGeometry class"""

    def __init__(self, size):
        """instantiation method"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size)

    def area():
        """area of the square"""

        return super().area()

    def __str__(self):
        """special method that returns the printable string"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

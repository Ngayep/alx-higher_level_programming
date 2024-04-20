#!/usr/bin/python3
"""child of hte base class"""


class Rectangle(Base):
    """Class with private attributes and constructor"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @getters
        def width(self):
            """width getter"""
            return self.__width

        def height(self):
            """height getter"""
            return self.__height

        @setters
        def width(self, value):
            """ width setter"""
            self.__width = value

        def height(self, value):
            """height setter"""
            self.__height = value

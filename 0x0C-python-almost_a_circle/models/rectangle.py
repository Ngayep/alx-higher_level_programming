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

        def x(self):
            """x getter"""
            return self.__x

        def y(self):
            """x getter"""
            return self.__y

        @setters
        def width(self, value):
            """ width setter"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        def height(self, value):
            """height setter"""
            if not isinstance(value, int):
                raise TypeError("heigth must be an integer")
            if heigth <= 0:
                raise ValueError("heigth must be > 0")
            self.__width = value

        def x(self, value):
            """x getter"""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        def y(self, value):
            """x getter"""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """returns area of rectangle"""
            return self.width * self.height

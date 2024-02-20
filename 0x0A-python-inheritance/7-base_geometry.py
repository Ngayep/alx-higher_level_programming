#!/usr/bin/python3
"""Geometry class"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """method that raises an Exception

        Args:
            self
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

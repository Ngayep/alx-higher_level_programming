#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""

        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, k)}
        return self.__dict__

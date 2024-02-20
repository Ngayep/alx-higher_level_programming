#!/usr/bin/python3
"""Checks if an object is same as class or as the one inherited from"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is same as class or as the one inherited from

    Args:
        obj: object to check
        a_class: class to compare the object to

    Returns True if object is an instance of or
        if the object is an instance of class inherited from
    """

    return isinstance(obj, a_class)

#!/usr/bin/python3
"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """returns True if object is exactly an instance of spcified class"""
    return type(obj) is a_class

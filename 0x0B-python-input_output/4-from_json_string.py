#!/usr/bin/python3
"""This module defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string"""

    data = json.loads(my_str)
    return data

#!/usr/bin/python3


def read_file(filename=""):
    """reads a text file and prints it to stdout"""

    with open(filename.txt, encoding="utf-8") as file:
        contents = file.read()
    print(contents, end="")

#!/usr/bin/python3


def write_file(filename="", text=""):
    """writes a string to a text file
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as file:
        count = file.write(text)
        return count

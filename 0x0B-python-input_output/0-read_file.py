#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (attempting UTF-8 encoding) and prints it to stdout.

    Args:
        filename: The name of the file to read.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

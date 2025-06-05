#!/usr/bin/python3
"""
This script defines a function to read and print the contents of a UTF-8 text file.

Usage:
    Call the read_file() function with a valid filename.
"""
def read_file(filename=""):
    """
    Print the contents of a UTF-8 text file to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")


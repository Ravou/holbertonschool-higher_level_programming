#!/usr/bin/python3
"""This module defines a Square class with printing and area calculation."""


class Square:
    """Represents a square with a size, area computation, and printed display."""

    def __init__(self, size=0):
        """Initialize the square with an optional size (default is 0)."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters, or an empty line if size is 0."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


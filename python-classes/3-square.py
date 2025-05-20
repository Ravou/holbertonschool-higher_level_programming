#!/usr/bin/python3
"""This module defines a Square class that validates size and computes area."""


class Square:
    """Represents a square with size validation."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): The size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2


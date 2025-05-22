#!/usur/bin/python3
"""Defines a Rectangle class with width and height"""

class Rectangle:
    """Class that defines a rectangle by width and height."""

    def __init(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.witdh = width
        self.height = height

    def width(self):
        """Getter for width"""
        return self.width

    def width(self, value):
        """Setter for width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Getter for height"""
        return self.__height

    def height(self, value):
        """Setter for height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

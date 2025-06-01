#!/usr/bin/pyhton3
""" Module that defines a base geometry class with validation methods.

This module contains:
- BaseGeometry: a base class with an unimplemented area method and a validator for intergers """


class BaseGeometry():
    """Base class for geometry abojects. """

    def area(self):
        """Raise an exception indicating that the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that `value` is a positive integer.

        Args:
            name (str): The name of the parameter (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

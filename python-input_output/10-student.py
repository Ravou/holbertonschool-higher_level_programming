#!/usr/bin/python3
"""Student class module
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.
        If attrs is a list of strings, only those attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                k: getattr(self, k)
                for k in attrs
                if hasattr(self, k)
            }
        return self.__dict__

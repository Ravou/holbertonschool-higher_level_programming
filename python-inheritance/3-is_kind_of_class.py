#!/usr/bin/python3
""" Use this for execute the function """
def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or a class that inherited from it."""
    return isinstance(obj, a_class)

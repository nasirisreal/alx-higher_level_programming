#!/usr/bin/python3
"""Defines a class and inherited class-check function."""


def is_kind_of_class(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class

    Args:
        obj (any): object
        a_class (type): class type
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    return isinstance(obj, a_class):
        return True
    return False

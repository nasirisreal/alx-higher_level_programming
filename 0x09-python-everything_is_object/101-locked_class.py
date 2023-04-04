#!/usr/bin/python3
"""
This module contains a class that prevents dynamically created attributes,
except for the 'first_name' attribute.
"""

class LockedClass:
    """
    A class that prevents dynamically created attributes,
    except for the 'first_name' attribute.
    """
    __slots__ = ['first_name']

    def __init__(self, first_name):
        """
        Initialize an instance of LockedClass with a first name.
        :param first_name: The first name of the instance.
        """
        self.first_name = first_name

    def __setattr__(self, key, value):
        """
        Set an instance attribute.
        :param key: The name of the attribute.
        :param value: The value to assign to the attribute.
        :raise: AttributeError if the attribute is not 'first_name'.
        """
        if key != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} does not allow setting attribute '{key}'")
        self.__dict__[key] = value

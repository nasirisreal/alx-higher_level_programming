#!/usr/bin/python3
"""

This is a module that containts a clas that avoids
dynmaically created attributes

"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(first_name):
        """
        Initialize an instance of LockedClass with a first name.
        :param first_name: The first name of the instance.
        """
        pass

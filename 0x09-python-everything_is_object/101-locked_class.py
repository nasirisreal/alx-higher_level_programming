#!/usr/bin/python3

class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} does not allow setting attribute '{key}'")
        self.__dict__[key] = value

#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} object has no attribute '{key}'")
        self.__dict__[key] = value

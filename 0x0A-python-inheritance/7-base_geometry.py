#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Class that defines the attributes of Geometric Shapes"""

    def area(self):
        """Method that defines the area of a geomtric shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that recieves the value property

        Árgs:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

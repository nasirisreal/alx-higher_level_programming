#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle from BaseGeometry Class"""

    def __init__(self, width, height):
        """Initializes instance"""

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return the print() and str() representation of a Rectangle."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

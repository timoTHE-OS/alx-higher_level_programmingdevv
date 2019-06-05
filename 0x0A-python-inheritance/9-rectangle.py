#!/usr/bin/python3
"""Module 9-rectangle.
Creates a Rectangle class.
"""


class BaseGeometry:
    """Class with public instance methods."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Public method area().
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance.

        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the Rectangle instance.
        Overwrites the area() method from BaseGeometry.
        """

        return self.__width * self.__height

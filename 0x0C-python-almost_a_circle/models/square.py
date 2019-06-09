#!/usr/bin/python3
"""Module square.
Create a Square class, inheriting from Rectangle.
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class describing a square.
    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            - __size: size
            - __x: position
            - __y: position
            - id: id
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""

        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)
        return s

    @property
    def size(self):
        """Retrieves the size attribute."""

        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates attributes of an instance.

        Args:
            - id attribute
            - size attribute
            - x attribute
            - y attribute
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                setattr(self, 'id', args[0])
            if len(args) > 1:
                setattr(self, 'size', args[1])
            if len(args) > 2:
                setattr(self, 'x', args[2])
            if len(args) > 3:
                setattr(self, 'y', args[3])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""

        my_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict

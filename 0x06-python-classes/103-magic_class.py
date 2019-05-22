#!/usr/bin/python3
class MagicClass:
    """Initialization of the MagicClass.
    Private methode __init__(self, radius=0)
    Public method area(self).
    Public method circumference(self).
    """
    def __init__(self, radius):
        """Initialization of the data."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculation of the area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculation of the circumference."""
        return 2 * math.pi * self._MagicClass__radius

#!/usr/bin/python3
"""Unittest for the Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class.
    Each method tests for a different input.
    """

    def test_2_id(self):
        """
        Check for id.
        """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 4, 5, "Hello")
        self.assertEqual(r4.id, "Hello")

    def test_2_values(self):
        """
        Check for attributes values.
        """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)

    def test_2_missing(self):
        """
        Check for missing arguments.
        """

        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional arguments: 'width' and 'height'", str(x.exception))

    def test_3_validation(self):
        """
        Check for attributes validation.
        """

        self.assertRaises(TypeError, Rectangle, "Hello", 2)
        self.assertRaises(TypeError, Rectangle, 2, "World")
        self.assertRaises(TypeError, Rectangle, 1, 2, "Foo", 3)
        self.assertRaises(TypeError, Rectangle, 3, 2, 2, "Bar")

        self.assertRaises(ValueError, Rectangle, 0, 4)
        self.assertRaises(ValueError, Rectangle, 8, -2)
        self.assertRaises(ValueError, Rectangle, 5, 2, -3, 0)
        self.assertRaises(ValueError, Rectangle, 9, 4, 8, -4)


if __name__ == '__main__':
    unittest.main()

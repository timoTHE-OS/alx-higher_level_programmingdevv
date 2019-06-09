#!/usr/bin/python3
"""Unittest base.
Test cases for Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test class for Base class.
    Each method tests for a different input.
    """

    def test_1_id(self):
        """Create new instances.
        Check for id.
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base("Hello")
        self.assertEqual(b4.id, "Hello")
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)


if __name__ == '__main__':
    unittest.main()

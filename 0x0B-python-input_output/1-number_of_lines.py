#!/usr/bin/python3
"""Module 1-number_of_lines.
Counts number of lines in a file.
"""


def number_of_lines(filename=""):
    """Counts lines in filename.

    Args:
        - filename: name of the file

    Returns:
        - number of lines
    """

    with open(filename) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

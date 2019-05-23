#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while text[i] == ' ':
        i += 1

    is_space = False

    for c in range(i, len(text)):
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            print("{}\n\n".format(text[c]), end='')
            is_space = True
            continue
        if is_space and text[c] == ' ':
            continue
        if is_space and text[c] != ' ':
            is_space = False
        print("{}".format(text[c]), end='')

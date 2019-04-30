#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper += chr(ord(c) - 32)
        else:
            upper += c
    print(upper)

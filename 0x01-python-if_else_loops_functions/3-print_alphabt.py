#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) is not 'e' or chr(letter) is not 'q':
        print("{}".format(chr(letter)), end="")

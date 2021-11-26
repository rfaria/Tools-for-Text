#!/usr/bin/env python3
"""
Tools for Text main.py
"""

from count import *
from menu import *

__author__ = "Rodrigo Candido Faria"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    choice = choose_func()

    if choice == "0":
        print("Selected: 0 - Count appearances of a character")
        print("Insert text: ")
        text = input()
        print("Insert character to be counted: ")
        charac = input()
        num = count_char_appearances(text, charac)

        print(f"The character {charac} appears {num} times in {text}")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
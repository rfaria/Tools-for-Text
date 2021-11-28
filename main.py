#!/usr/bin/env python3
"""
Tools for Text main.py
"""

from count import *
from edit import *
from menu import *
from sentiment import *

__author__ = "Rodrigo Candido Faria"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    while(1):
        choice = choose_func()

        if choice == "0":
            print("Selected: 0 - Count appearances of a character in a manually inputed text")
            print("Insert text: ")
            text = input()
            print("Insert character to be counted: ")
            charac = input()
            num = count_char_appearances_manual_text(text, charac)

            print(f"The character \"{charac}\" appears {num} times in \"{text}\".\n\n")

        elif choice == "1":
            print("Selected: 1 - Total number of characters in a manually inputed text")
            print("Insert text: ")
            text = input()
            size = length_of_text(text)

            print(f"The text \"{text}\" has {size} characters.\n\n")
        
        elif choice == "2":
            print("Selected: 2 - Swap words in a text")
            print("Insert text: ")
            text = input()
            print("Insert word to be deleted: ")
            old_word = input()
            print("Insert word to be added: ")
            new_word = input()
            new_text = swap_words(text, old_word, new_word)

            print(f"The new text is: \"{new_text}\"\n\n")
        
        elif choice == "3":
            print("Selected: 3 - Extract global text sentiment")
            print("Insert text: ")
            text = input()
            result = global_sentiment(text)
            
            print(f"\nThe global text sentiment is: \"{result}\"\n\n")

        elif choice == "4":
            print("Selected: 4 - Extract sentiment of each word")
            print("Insert text: ")
            text = input()
            result = sentiment_word_list(text)

            neg = result["negative"]
            neu = result["neutral"]
            pos = result["positive"]
            
            print(f"\nThe negative words are: \"{neg}\"\n")
            print(f"The neutral words are: \"{neu}\"\n")
            print(f"The positive words are: \"{pos}\"\n")

        elif choice == "quit":
            break


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
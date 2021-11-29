#!/usr/bin/env python3
"""
Tools for Text main.py
"""

# conda list --export > requirements.txt
# conda env export > environment.yml
# conda env export > app.yaml

from count import *
from edit import *
from menu import *
from sentiment import *
from lang_detect import *
# from flask import Flask

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Congratulations, it's a web app!"

__author__ = "Rodrigo Candido Faria"
__version__ = "0.1.0"
__license__ = "MIT"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    """ Main entry point of the app """
    while(1):
        choice = choose_func()

        if choice == "0":
            print(f"{bcolors.OKBLUE}Selected: 0 - Count appearances of a character in a manually inputed text{bcolors.ENDC}")
            print("Insert text: ")
            text = input()
            print("Insert character to be counted: ")
            charac = input()
            num = count_char_appearances_manual_text(text, charac)

            print(f"{bcolors.OKGREEN}The character \"{charac}\" appears {num} times in \"{text}\".\n{bcolors.ENDC}")

        elif choice == "1":
            print(f"{bcolors.OKBLUE}Selected: 1 - Total number of characters in a manually inputed text{bcolors.ENDC}")
            print("Insert text: ")
            text = input()
            size = length_of_text(text)

            print(f"{bcolors.OKGREEN}The text \"{text}\" has {size} characters.\n\n{bcolors.ENDC}\n")
        
        elif choice == "2":
            print(f"{bcolors.OKBLUE}Selected: 2 - Swap words in a text{bcolors.ENDC}")
            print("Insert text: ")
            text = input()
            print("Insert word to be deleted: ")
            old_word = input()
            print("Insert word to be added: ")
            new_word = input()
            new_text = swap_words(text, old_word, new_word)

            print(f"{bcolors.OKGREEN}The new text is: \"{new_text}\"\n{bcolors.ENDC}")
        
        elif choice == "3":
            print(f"{bcolors.OKBLUE}Selected: 3 - Extract global text sentiment{bcolors.ENDC}")
            print("Insert text: ")
            text = input()
            result = global_sentiment(text)

            if result == "Negative":         
                print(f"\n{bcolors.FAIL}The global text sentiment is: \"{result}\"\n{bcolors.ENDC}")
            elif result == "Neutral":
                print(f"\n{bcolors.WARNING}The global text sentiment is: \"{result}\"\n{bcolors.ENDC}")
            else:
                print(f"\n{bcolors.OKGREEN}The global text sentiment is: \"{result}\"\n{bcolors.ENDC}")

        elif choice == "4":
            print(f"{bcolors.OKBLUE}Selected: 4 - Extract sentiment of each word{bcolors.ENDC}")
            print("Insert text: ")
            text = input()
            result = sentiment_word_list(text)

            neg = result["negative"]
            neu = result["neutral"]
            pos = result["positive"]
            
            print(f"\n{bcolors.FAIL}The negative words are: \"{neg}\"\n{bcolors.ENDC}")
            print(f"{bcolors.WARNING}The neutral words are: \"{neu}\"\n{bcolors.ENDC}")
            print(f"{bcolors.OKGREEN}The positive words are: \"{pos}\"\n{bcolors.ENDC}")
        
        elif choice == "5":
            print(f"{bcolors.OKBLUE}Selected: 5 - Detect a text language{bcolors.ENDC}")
            print("Insert text: ")
            text = input()
            result = detect_language(text)

            print(f"\n{bcolors.OKGREEN}Language detected: \"{result[0]}\"{bcolors.ENDC}")
            print(f"{bcolors.OKGREEN}Probability: {result[1]}\n{bcolors.ENDC}")

        elif choice == "quit":
            break

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

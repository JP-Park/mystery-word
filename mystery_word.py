import random
import re
from collections import Counter

print("Welcome to Mystery-Word! Guess the word in less than 8 tries. ")

with open("/usr/share/dict/words", "r") as word_List:

    def easy_game_words():
        easy_words = []
        for word in word_List:
            x = len(word)
            if x >= 4 and x <= 6:
                easy_words.append(word.strip().lower())
        return easy_words

    def med_game_words():
        med_words = []
        for word in word_List:
            x = len(word)
            if x >= 6 and x <= 8:
                med_words.append(word.strip().lower())
        return med_words

    def hard_game_words():
        hard_words = []
        for word in word_List:
            x = len(word)
            if x >= 8:
                hard_words.append(word.strip().lower())




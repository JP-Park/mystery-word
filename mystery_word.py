import random
import re
from collections import Counter

with open("/usr/share/dict/words", "r") as wordList:
    for word in wordList:
        x = len(word.strip())
        if x >= 4 and x <= 6:
            print(word.lower())


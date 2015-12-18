import os
import random
import sys


def easy_game_words():
    easy_words = []
    with open("/usr/share/dict/words", "r") as word_List:
        for word in word_List:
            if len(word) >= 4 and len(word) <= 6:
                easy_words.append(word.strip().lower())
        the_word = random.choice(easy_words)
        return the_word


def med_game_words():
    med_words = []
    with open("/usr/share/dict/words", "r") as word_List:
        for word in word_List:
            if len(word) >= 6 and len(word) <= 8:
                med_words.append(word.strip().lower())
        the_word = random.choice(med_words)
        return the_word


def hard_game_words():
    hard_words = []
    with open("/usr/share/dict/words", "r") as word_List:
        for word in word_List:
            if len(word) > 8:
                hard_words.append(word.strip().lower())
        the_word = random.choice(hard_words)
        return the_word


def game_type():
    game_mode = input("Please select Easy, Med, or Hard: ").lower()

    if game_mode == 'easy' or game_mode == 'e':
        easy_word = easy_game_words()
        return easy_word

    elif game_mode == 'med' or game_mode == 'm':
        med_word = med_game_words()
        return med_word

    elif game_mode == 'hard' or game_mode == 'h':
        hard_word = hard_game_words()
        return hard_word

    else:
        print("That was not a valid selection ")
        return game_type()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print("Guesses left: {}/8".format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_ ', end='')

    print('')


def get_guess(bad_guesses, good_guesses):
    while True:
        # take guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a string letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guess that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess


def play(done):
    clear()
    secret_word = game_type()
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True

        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 8:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()


def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True

print('Welcome to Letter Guess!')

done = False

while True:
    clear()
    welcome()
    play(done)
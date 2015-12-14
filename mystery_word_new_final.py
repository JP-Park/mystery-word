import random

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



def player_guess():
        guess = input("Please guess a letter: ").upper()
        
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("That was not a valid guess!")


def display_word(game_word, guessed_letters):
    magic_word = []
    for letter in game_word:
        if letter in guessed_letters:
            magic_word.append(letter.upper())
        else:
            magic_word.append("_")
    show_word = (" ".join(magic_word))
    return show_word
    

def game():
    guess_count = 0
    guessed_letters = []
    game_word = game_type()
    show = display_word(game_word, guessed_letters)

    while guess_count < 8:
        guess = player_guess()
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            guess_count += 1
            print(show)
            continue
        else:
            print("You already guessed that letter!")

    else:
        print('Your word was {}'.format(game_word.upper()))
        again = input('Would you like to play again? ')
        if again == 'y':
            game()
        elif again == 'n':
            running = False
            print("Thank you for playing!")
        else:
            print("That was not a valid choice....")
            


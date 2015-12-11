"""built in function as it says... randomly import variables"""
import random


"""define function and giving a variable named easy_game_words"""
def easy_game_words():
"""ways to enter a list called easy_words"""
    easy_words = []
"""using with statement to open/read the file/source and called as word_list"""
    with open("/usr/share/dict/words", "r") as word_List:
"""using for loops and give word a name"""
        for word in word_List:
"""using if statement to give and define the length of word between 4-6 """
            if len(word) >= 4 and len(word) <= 6:
"""add lower cased and white space stripped word. called easy_words"""
                easy_words.append(word.strip().lower())
"""randomly choose a word send to a variable called the_word"""
        the_word = random.choice(easy_words)
"""set variable named the_word"""
        return the_word

"""define function and giving a variable named med_game_words"""
def med_game_words():
"""ways to enter a list called med_words"""
    med_words = []
"""using with statement to open/read the file/source and called as word_list"""
    with open("/usr/share/dict/words", "r") as word_List:
"""using for loops and give word a name"""
        for word in word_List:
"""using if statement to give and define the length of word between 6-8 """
            if len(word) >= 6 and len(word) <= 8:
"""add lower cased and white space stripped word. called med_words"""
                med_words.append(word.strip().lower())
"""randomly choose a word send to a variable called the_word"""
        the_word = random.choice(med_words)
"""set variable named the_word"""
        return the_word

"""define function and giving a variable named med_game_words"""
def hard_game_words():
"""ways to enter a list called med_words"""
    hard_words = []
"""using with statement to open/read the file/source and called as word_list"""
    with open("/usr/share/dict/words", "r") as word_List:
"""using for loops and give word a name"""
        for word in word_List:
"""using if statement to give and define the length of word 8 and more"""
            if len(word) > 8:
"""add lower cased and white space stripped word. called hard_words"""
                hard_words.append(word.strip().lower())
"""randomly choose a word send to a variable called the_word"""
        the_word = random.choice(hard_words)
"""returns and set variable named the_word"""
        return the_word

"""define function giving a variable named game_type"""
def game_type():
"""asking to choose a game more and it returns lower cased alphabet. called game_mode"""
    game_mode = input("Please select Easy, Med, or Hard: ").lower()
"""if statement, player is able to choose the game more as easy or e"""
    if game_mode == 'easy' or game_mode == 'e':
"""give a variable to easy_word"""
        easy_word = easy_game_words()
"""returns and set variable named easy_word"""
        return easy_word
"""else if... player choose med or m, than it will player Med mode"""
    elif game_mode == 'med' or game_mode == 'm':
"""give a variable to med_words"""
        med_word = med_game_words()
"""returns and set variable named med_word"""
        return med_word
"""else if... player choose hard or h, than it will player Hard mode"""
    elif game_mode == 'hard' or game_mode == 'h':
"""give a variable to hard_words"""
        hard_word = hard_game_words()
"""returns and set variable named hard_word"""
        return hard_word
"""else statement... always at the end"""
    else:
"""ask to print the string"""
        print("That was not a valid selection ")
"""returns and set variable named game_type"""
        return game_type()


"""define function giving a variable named player_guess"""
def player_guess():
"""choose a letter and input as upper cased letter and called guess"""
        guess = input("Please guess a letter: ").upper()
"""if alphabet was chosen, 1 guess have been used"""
        if guess.isalpha() and len(guess) == 1:
"""returns and set variable named guess"""
            return guess
"""else statement... always at the end"""
        else:
"""print the strings"""
            print("That was not a valid guess!")

"""define function giving a variable named display_word and give two arguments"""
def display_word(game_word, guessed_letters):
"""giving an empty list"""
    magic_word = []
"""for loops find letter inside of game_word"""
    for letter in game_word:
"""if statement... if the letter is in guessed_letters"""
        if letter in guessed_letters:
"""add an upper cased letter to magic_word"""
            magic_word.append(letter.upper())
"""else statement... always at the end"""
        else:
"""magic_word is going to add "_" """
            magic_word.append("_")
"""taking list of the things and join with strings"""
    show_word = (" ".join(magic_word))
"""returns and set variable named show_word"""
    return show_word

"""define the game and how it plays"""
def game():
"""start with zero count"""
    guess_count = 0
"""assign an empty list"""
    guessed_letters = []
"""set game_type as tuple"""
    game_word = game_type()
"""returns key and value called display_word... send to show"""
    show = display_word(game_word, guessed_letters)
"""while statement if the count is less than 8"""
    while guess_count < 8:
"""give guess number of tries"""
        guess = player_guess()
"""if statement guessed_letter in NOT in guess"""
        if guess not in guessed_letters:
"""guessed_letters add to guess"""
            guessed_letters.append(guess)
"""after the try add 1 try has been added"""
            guess_count += 1
"""print the show"""
            print(show)
"""continuing the function"""
            continue
"""else statement... always at the end"""
        else:
"""print the strings"""
            print("You already guessed that letter!")
"""else statement... always at the end"""
    else:
"""{} display word, formatted in upper case"""
        print('Your word was {}'.format(game_word.upper()))
"""input a strings and give a value to agian"""
        again = input('Would you like to play again? ')
"""if statement again is absolute y"""
        if again == 'y':
"""than game will start again as a new game"""
            game()
"""else if... again is absolute n"""
        elif again == 'n':
"""boolean False"""
            running = False
"""print the strings"""
            print("Thank you for playing!")
"""else statement... always at the end"""
        else:
"""print the string"""
            print("That was not a valid choice....")



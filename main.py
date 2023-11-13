import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

global guesses_left
global chosen_word
global guess

#Begin Game
def begin_game():
    #Choose word
    chosen_word = random.choice(word_list)
    guesses_left = 6
    display = []

    #Display
    print(logo)
    length = len(chosen_word)
    for i in range(0,length):
        display += "_"

    print(display)
    game(chosen_word, guesses_left, display, length)

def game(chosen_word, guesses_left, display, length):
    guess = input("Guess a letter!\n")
    if guess not in chosen_word:
        score("no", display, guesses_left, chosen_word, length)

    else:
        for j in range(0,length):
            if guess == chosen_word[j]:
                display[j] = guess

        print(display)

        score("yes", display, guesses_left, chosen_word, length)


def score(correct, display, guesses_left, chosen_word, length):
    if correct == "yes":
        if display.count("_") == 0:
            print("You win!")

        else:
            game(chosen_word, guesses_left, display, length)
    else:
        guesses_left -= 1

        print(stages[guesses_left])

        if guesses_left > 0:
            print(f"You have {guesses_left} guesses left!")

            game(chosen_word, guesses_left, display, length)

        else:
            print(f"You have {guesses_left} guesses left!")
            print("Game Over!")

begin_game()






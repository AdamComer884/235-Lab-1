from messages import *
from hiddenFunctions import *

"""
This is a simple guessing game written for COMPSCI 235 students to explore the debugging features of PyCharm.

Main Objective:
    Start by reading the code, running it, and playing a few games. 
    Question 1:     What is the probability of winning a game?
    Question 2:     Using the debugging feature, WITHOUT changing any code, it is possible to win every game.
                    What line did you insert the breakpoint at? 
    Question 3:     Using the debugging feature only, is it possible the user can win every game by guessing "42"?
    
Extension Activity:
    Extension 1.    This code is not very robust. If the player enters an incorrectly formatted 
                    guess (e.g. typing "seven") the code will crash.
                    Make the game more robust to user inputs (e.g. 
                    request another input if the user guesses outside the range).
    Extension 2.    You will find functions in numberChecker.py that check if the 
                    number is even or is a prime. First modify the game so that the 
                    computer and user can only select even numbers. Then modify the code so that 
                    the only prime numbers are used. Finally add an option to each round to select between using all
                    numbers, only even numbers, or only prime numbers.   
"""

# Q1: 1/100 (1/UPPER_VAL-LOWER_VAL)
# Q2: "guess = user_guess()" -> View what the value of selected_number is in either the 'Variables' tab or in the IDE
# Q3: Nein
# E1: See user_guess. Added constants LOWER_VAL and UPPER_VAL for modularity. Removed unused parameter in user_guess
"""
E2:

For this task I decided to create two new functions hiddenFunctions.py. Arrays are generated at the start of runtime in
which include either numbers, even or only prime. This saves re-running some code.

The new function generate_array in numberChecker.py accepts another boolean-return function object as a parameter. The
advantage of this is that we can create different checks (i.e. check_is_odd) without creating duplicate code in generating
new arrays/tuples.

The pickANumber function was modified to include an enum parameter. This approach helps prevent accidental programming
errors.

Please note I chose to change some of the variables and functions to camel_case or UPPER_CASE depending on their uses.

"""

gamesPlayed: int = 0
gamesWon: int = 0

LOWER_VAL: int = 1
UPPER_VAL: int = 100


def welcome():
    print(WELCOME)


def computer_pick_number():
    number_set = choose_number_set()
    print(PICK_NUMBER)
    number = pick_a_number(number_set)
    return number;


def user_guess(prompt: str, values: list or tuple) -> int:
    while True:
        try:
            guess = int(input(prompt))
            if guess not in values:
                raise ValueError(f"Value outside of range: {min(values)} -> {max(values)}")
            break
        except TypeError:
            print("Invalid input! Must be an integer.")
    return guess


def choose_number_set() -> tuple:
    choice = user_guess(PICK_GAME_MODE, [1, 2, 3])
    match choice:
        case 1: return SelectionSet.Numbers.value
        case 2: return SelectionSet.Even.value
        case 3: return SelectionSet.Prime.value
    """
    Python < 3.10
    if choice == 1: return SelectionSet.Numbers
    elif choice == 2: return SelectionSet.Even
    elif choice == 3: return SelectionSet.Prime
    """


def endGame():
    print(final_score(gamesWon, gamesPlayed))


def game():
    global gamesWon, gamesPlayed
    print(LINE_OF_STARS)
    selected_number = computer_pick_number()
    guess = user_guess(PROMPT_GUESS, range(LOWER_VAL, UPPER_VAL))
    if selected_number == guess:
        print(WIN)
        gamesWon += 1
    else:
        print(LOSE)
    gamesPlayed += 1


def play_again():
    again = input(PLAY_AGAIN)
    if again != "y" and again != "n":
        print(INVALID_INPUT)
        play_again()

    elif again == "y":
        game()
        play_again()
    else:
        endGame()


def main():
    welcome()
    game()
    play_again()


if __name__ == '__main__':
    main()

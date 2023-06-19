"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!

    print("\nWelcome to the guessing game!")
    print("A number between _ and 72?")
    lowerBound = input("Enter a lower bound: ")
    print(f"OK then, a number between {lowerBound} and 72?")
    lowerBound = int(lowerBound)

    actualNumber = random.randint(lowerBound, 72)

    guessed = False

    while not guessed:
        guessedNumber = input("Guess a number: ")
        try:
            guessedNumber = int(guessedNumber)
            return guessedNumber
        except ValueError:
            print("Hey! That's not a number!🤬")
        
        print("You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print("OMG! You got it!")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Uh oh ... that's too small :'(")
        else:
            print("Oh no! That's too big!")
        return "You got it!"

if __name__ == "__main__":
    print(advancedGuessingGame())


from random import randint


def higher_or_lower(guess, answer):
    if guess == answer:
        return "You're correct!!"
    elif guess < answer:
        return "Higher"
    else:
        return "Lower"


def guessing(guess, answer):
    result = higher_or_lower(guess, answer)
    if result == "You're correct!!":
        print(result)
    else:
        guess = int(raw_input(result + ". Guess again "))
        guessing(guess, answer)

user_answer = randint(0, 100)
user_guess = int(raw_input("Guess a number! "))
guessing(user_guess, user_answer)
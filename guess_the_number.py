from art import logo8
import random
from replit import clear

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_diff():
    level = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check(guess, answer):
    if guess > answer:
        print("Too high.\nGuess again.")
    elif guess < answer:
        print("Too low.\nGuess again.")
    else:
        print(f"You got it! The answer was {answer}.")
        return True

def game():
    print(logo8)
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

    num = random.randint(1, 100)
    attempts = set_diff()

    end_of_game = False
    while not end_of_game:
        if attempts == 0:
            end_of_game = True
            print(f"You've run out of attempts. The number was {num}. Game Over...")
            break

        print(f"You have {attempts} attempts remaining to guess the number.")

        user_guess = int(input("Make a guess: "))

        if check(user_guess, num):
            break
        attempts -= 1

    play_again = False
    while not play_again:
        again = input("Try again? Type 'y' or 'n': ")
        if again == 'y':
            play_again = True
            clear()
            game()
        elif again == 'n':
            play_again = True
            clear()
game()
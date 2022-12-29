import random
from words import easy, hard, harder
from art import stage, logo5
from replit import clear

stages = stage
difficulty = int(input("Please choose a difficulty. Enter 1 for easy, 2 for hard, or 3 for harder: "))
word_list = None
if difficulty not in range(1, 3):
    print('Not a valid selection')
elif difficulty == 1:
    word_list = easy
elif difficulty == 2:
    word_list = hard
elif difficulty == 3:
    word_list = harder

chosen_word = random.choice(word_list)

lives = 6
end_of_game = False
display = list()

for letters in chosen_word:
    display.append('_')

print(logo5)
print(stages[lives])
print(''.join(display))

while not end_of_game:
    user_choice = input("Guess a letter: ").lower()

    clear()

    if user_choice in display:
        print("You've already tried that letter.")
        print(''.join(display))

    for index, letter in enumerate(chosen_word):
        if letter == user_choice:
            display[index] = letter
            print(f"You've guessed {user_choice}, that letter is in the word!")

    if user_choice not in chosen_word:
        lives -= 1
        print(f"You've guessed {user_choice}, that letter is not in the word. You lose a life.")

    print(stages[lives])
    print(''.join(display))

    if lives == 0:
        print('You lose!')
        print(f"The word was {chosen_word}")
        end_of_game = True

    if '_' not in display:
        print('You win!') 
        end_of_game = True       
    
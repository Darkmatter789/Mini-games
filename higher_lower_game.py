import random
from replit import clear
from art import logo9, logo10
from higher_lower_data import data

clear()

def get_b():
    return data[random.randint(0, len(data))]

def compare_counts(a, b):
    if a > b:
        return 'a'
    else:
        return 'b'

def game():
    score = 0
    comp_a = data[random.randint(0, (len(data) - 1))]
    print(logo9)
    game_over = False
    while not game_over:
        comp_b = get_b()
        follower_count_a = comp_a['follower_count']
        follower_count_b = comp_b['follower_count']
        answer = compare_counts(follower_count_a, follower_count_b)
    
        print(f"Compare A: {comp_a['name']}, a {comp_a['description']}, from {comp_a['country']}.")
        print(logo10)
        print(f"Against B: {comp_b['name']}, a {comp_b['description']}, from {comp_b['country']}.")
        print(answer)

        user = input("Who has more followers? Type 'A' or 'B': ").lower()
    
        if user == answer:
            comp_a = comp_b
            score += 1
            clear()
            print(logo9)
            print(f"Your right! Current score: {score}.")
        else:
            clear()
            print(logo9)
            print(f"You typed '{user.upper()}'. Sorry, that's wrong. Answer was '{answer.upper()}'. Final score: {score}")
            game_over = True

    play_again = False
    while not play_again:
        again = input("Would you like to play again? 'y' or 'n'?: ")
        if again == 'y':
            play_again = True
            clear()
            game()
        elif again == 'n':
            play_again = True
            clear()    
game()
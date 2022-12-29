import random
from colorama import Fore
from art import logo4

user_win_count = 0
comp_win_count = 0
draw_count = 0
win_pct = 0

while True:    

    user_choice = int(input("Lets play Rock, Paper, Scissors. Type 0 for Rock, 1 for paper, and 2 for Scissors: "))
    computer_choice = random.randint(0, 2)

    if user_win_count > 0 or comp_win_count > 0 or draw_count > 0:
        win_pct = float(user_win_count) / float(user_win_count + comp_win_count + draw_count)

    if user_choice > 2 or user_choice < 0:
        print("Thats not a valid choice. You lose by default")
        quit()

    print(f'{logo4[user_choice]}\nYour choice:\n{logo4[computer_choice]}\nComputer choice:''')

    if user_choice == computer_choice:
        draw_count += 1
        print(f'Its a draw\nYour wins: {user_win_count}\nComputer wins: {comp_win_count}\nDraws: {draw_count}\nwin pct: {win_pct}%')
    elif user_choice == 0 and computer_choice == 2:
        user_win_count += 1
        print(f'You win!\nYour wins: {user_win_count}\nComputer wins: {comp_win_count}\nDraws: {draw_count}\nwin pct: {win_pct}%')
    elif user_choice == 2 and computer_choice == 0:
        comp_win_count += 1
        print(f'You lose!\nYour wins: {user_win_count}\nComputer wins: {comp_win_count}\nDraws: {draw_count}\nwin pct: {win_pct}%')
    elif user_choice > computer_choice:
        user_win_count += 1
        print(f'You win!\nYour wins: {user_win_count}\nComputer wins: {comp_win_count}\nDraws: {draw_count}\nwin pct: {win_pct}%')
    elif user_choice < computer_choice:
        comp_win_count += 1
        print(f'You lose!\nYour wins: {user_win_count}\nComputer wins: {comp_win_count}\nDraws: {draw_count}\nwin pct: {win_pct}%')

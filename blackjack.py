import random
from art import logo7
from replit import clear
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hit(player):
     player.append(random.choice(cards))
     print(player)


def blackjack():
    print(logo7)

    player_cards = random.choices(cards, weights=None, cum_weights=None, k=2)
    computer_cards = random.choices(cards, weights=None, cum_weights=None, k=1)
    print(f"Dealer cards: {computer_cards}")
    print(f"Your cards: {player_cards}")

    gameover = False
    while not gameover:
        player_total = sum(player_cards)
        dealer_total = sum(computer_cards)

        player_turn = True
        while player_turn:
            player_total = sum(player_cards)
            if 11 in player_cards and player_total > 21:
                player_cards.remove(11)
                player_cards.append(1)

            player_total = sum(player_cards)
            if player_total > 21:
                print(f"You have {player_total}. You busted! Dealer wins!")
                player_turn = False
            elif player_total == 21:
                player_turn = False
                print("You have 21. Dealer's turn.")
            elif player_total < 21:
                hit_or_stand = input(f"You have {player_total}. Would you to hit or stay? Type 'h' or 's': ").lower()
                if hit_or_stand == 'h':
                    hit(player_cards)
                elif hit_or_stand == 's':
                    player_turn = False
                    hit(computer_cards)

        if player_total > 21:
            gameover = True
        else:
            dealer_turn = True
            while dealer_turn:
                dealer_total = sum(computer_cards)
                if 11 in computer_cards and dealer_total > 21:
                    computer_cards.remove(11)
                    computer_cards.append(1)

                dealer_total = sum(computer_cards)
                if dealer_total > 21:
                    print(f"Dealer has {dealer_total}. Dealer busted. You win!")
                    dealer_turn = False
                    gameover = True
                elif dealer_total < 17 or dealer_total < player_total:
                    hit(computer_cards)
                elif dealer_total > 16 and dealer_total < 22:
                    dealer_turn = False

            if dealer_total > 21:
                gameover = True
            else:    
                if player_total > dealer_total:
                    print(f"You have {player_total} and dealer has {dealer_total}. You win!")
                    gameover = True
                elif player_total == dealer_total:
                    print(f"You have {player_total} and dealer has {dealer_total}. It's a draw!")
                    gameover = True
                else:
                    print(f"You have {player_total} and dealer has {dealer_total}. You lose!")
                    gameover = True
        

    play_again = False
    while not play_again:
        again = input("Would you like to play again? 'y' or 'n'?: ")
        if again == 'y':
            play_again = True
            clear()
            blackjack()
        elif again == 'n':
            play_again = True
            clear()

start = input("Would you like to play BlackJack? 'y' or 'n'?: ").lower()

if start == 'y':
    blackjack()
else:
    clear()
from art import logo3

print(logo3)
print('''...........Welcome...........
              to
        Treasure Island!   
Your mission is to find the treasure.''')

first = input("You are walking down a trail and come to a fork. Do you go 'left' or 'right'?:\n").lower()
if first == "left":
    second = input("You come to a lake with an island in the middle. Do you 'swim' or 'wait' for a boat?:\n").lower()
    if second == "wait":
        third = input('''You made it to the island. 
You walk to the middle of the island and come to an abandonded town.
You see a big building with three doors, one 'yellow', one 'blue, and one 'red'.
which door do you pick?:\n''').lower()
        if third == "yellow":
            print("You found the treasure room! YOU WIN!!!!!")
        elif third == "blue":
            print("The floor opens beneath you and you fall into a pool full of crocs! GAME OVER!!!")
        elif third == "red":
            print("You open the 'red' door and a beast jumps out and tears you to shreds. GAME OVER!!!")
        else:
            print('Not a valid response. YOU LOSE by default!!!')
    else:
        print("You were swallowed by a giant fish. GAME OVER!!!")
else:
    print("You ran into a pack of hungry wolves. You've been eaten. GAME OVER!!!")
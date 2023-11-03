import random
import ascii_art

# 0 - Rock
# 1 - Paper
# 2 - Scissors

def game():
    computers_decision = random.randint(0, 2)
    possible_outcomes = [ascii_art.rock, ascii_art.paper, ascii_art.scissors]
    users_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

    computers_choice = possible_outcomes[computers_decision]
    users_choice = possible_outcomes[users_decision]

    if computers_decision == 0 and users_decision == 1:
        printChoice(computers_choice, users_choice)
        print("You win!")
    elif computers_decision == 0 and users_decision == 2:
        printChoice(computers_choice, users_choice)
        print("Computer won! You loose!")
    elif computers_decision == 1 and users_decision == 0:
        printChoice(computers_choice, users_choice)
        print("Computer won! You loose!")
    elif computers_decision == 1 and users_decision == 2:
        printChoice(computers_choice, users_choice)
        print("You win!")
    elif computers_decision == 2 and users_decision == 0:
        printChoice(computers_choice, users_choice)
        print("You win!")
    elif computers_decision == 2 and users_decision == 1:
        printChoice(computers_choice, users_choice)
        print("Computer won! You loose!")
    else:
        printChoice(computers_choice, users_choice)
        print("It's a tie!")


def printChoice(computers_choice, users_choice):
    print(f"You chose: \n {users_choice} \n Computer chose: \n {computers_choice} \n")


try:
    game()
except Exception:
    print('Type 0 for Rock, 1 for Paper or 2 for Scissors.')
    game()

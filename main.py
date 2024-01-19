import random

total_games = 0
total_repeats = 0
player_wins = 0
computer_wins = 0
equal = 0

while True:
    total_games += 1
    total_repeats += 1


    while True:
        user_choice = input("Change: rock, scissor or papper: ").lower()
        if user_choice == "rock" or user_choice == "scissor" or user_choice == "papper":
            break
        else:
            print("Invalid selection. Please, try again.")

    computer_choice = random.choice(["rock", "scissor", "papper"])

    print(f"The player chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        winner = "Drow"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "papper") or \
         (user_choice == "papper" and computer_choice == "rock"):
        winner = "player"
    else:
        winner = "computer"

    if winner == "player":
        player_wins += 1
        print(f"You win!")
    elif winner == "computer":
        computer_wins += 1
        print(f"You lost!")
    else:
        print(f"Drow!")
        equal += 1

    print(f"Results: \nplayer wins: {player_wins}, computer wins: {computer_wins}, "
          f"\nEqualities {equal} game out of a total of {total_games} games")

    play_again_choice = input("Do you want to play again (y/n)? ").lower()
    if play_again_choice != "yes":
        print("Thanks for the game!")
        break

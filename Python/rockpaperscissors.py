import random

def play_game():
    choices = ['r', 'p', 's']
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose {translate_choice(user_choice)}, the computer chose {translate_choice(computer_choice)}.")

        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            user_score += 1
            print(f"{translate_choice(user_choice)} {get_action(user_choice)} {translate_choice(computer_choice)}! You win.")
        elif result == "lose":
            computer_score += 1
            print(f"{translate_choice(computer_choice)} {get_action(computer_choice)} {translate_choice(user_choice)}! You lose.")
        else:
            print(f"Both players selected {translate_choice(user_choice)}. It's a tie!")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\nFinal Scores:")
    print(f"Computer: {computer_score}")
    print(f"Player: {user_score}")

def translate_choice(choice):
    if choice == 'r':
        return 'Rock'
    elif choice == 'p':
        return 'Paper'
    elif choice == 's':
        return 'Scissors'

def determine_winner(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return "win"
    elif (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
        return "lose"
    else:
        return "tie"

def get_action(choice):
    if choice == 'r':
        return 'smashes'
    elif choice == 'p':
        return 'covers'
    elif choice == 's':
        return 'cuts'

# Start the game
play_game()

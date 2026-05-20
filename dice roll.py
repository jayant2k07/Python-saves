import random

def roll_dice():
    # Function to roll the dice and return a random number between 1 and 6
    return random.randint(1, 6)

def play_game():
    print("=" * 40)
    print("Welcome to the Dice Roll Game!")
    print("=" * 40)
    
    while True:
        # Ask user if they want to roll the dice
        choice = input("\nDo you want to roll the dice? (yes/no): ").lower().strip()
        
        if choice in ['yes', 'y']:
            # Roll the dice for player and computer, then compare
            user_result = roll_dice()
            computer_result = roll_dice()
            print(f"You rolled: {user_result}")
            print(f"Computer rolled: {computer_result}")

            if user_result > computer_result:
                print("You win!")
            elif user_result < computer_result:
                print("Computer wins!")
            else:
                print("It's a tie!")
        elif choice in ['no', 'n']:
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Run the game
play_game()

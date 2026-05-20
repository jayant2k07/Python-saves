import random

def get_computer_choice():
    # Get a random choice for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    # Get the player's choice with validation
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def determine_winner(player, computer):
    # Determine the winner of the game. compare choices 
    if player == computer:
        return "tie"
    elif player == "rock" and computer == "scissors":
        return "player"
    elif player == "paper" and computer == "rock":
        return "player"
    elif player == "scissors" and computer == "paper":
        return "player"
    else:
        return "computer"

def display_result(player, computer, result):
    # Display the game result
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    # Main game loop
    while True:
        print("\n" + "="*40)
        print("Welcome to Rock Paper Scissors!")
        print("="*40)
        
        # Get choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        # Display result
        display_result(player_choice, computer_choice, result)
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

play_game()

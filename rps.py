import random
import os

# Get random computer choice
def get_computer_choice():
	computer_choices = ["rock", "paper", "scissors"]
	return random.choice(computer_choices)

def get_user_choice():
	user_choices = {1:"rock", 2:"paper", 3:"scissors"}
	try:
		user_input = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
		if user_input in user_choices:
			return user_choices[user_input]
		else:
			print("Invalid choice. Please try again.")
			return get_user_choice()

	except ValueError:
		print("Invalid input. Please enter a number between 1 and 3.")
		return get_user_choice()

# Determine winner
def determine_winner(user_choice, computer_choice):
	if user_choice == computer_choice:
		return "It's a tie!"
	# Determine user winning
	elif (user_choice == "rock" and computer_choice == "scissors") or \
		 (user_choice == "paper" and computer_choice == "rock") or \
		 (user_choice == "scissors" and computer_choice == "paper"):
		return "Alright alright, you beat me. Congratulations, winner."
	else:
		return "Ha! In your face! I win!!!"

# Play again function
def play_again():
	while True:
		user_input = input("Do you want to play again? Y/N: ").upper()
		# Logic for choice
		if user_input in ['Y', 'YES', 'N', 'NO']:
			return user_input == "Y"
		else:
			print("Invalid input. Please enter 'Y' or 'N'.")

# Set up game
def play_game():
	while True:
		# Clear the screen
		os.system("clear")

		# Get user choice
		user_choice = get_user_choice()
		# Get computer choice
		computer_choice = get_computer_choice()

		# Ouptut summary
		print(f"You chose {user_choice.upper()} and the I chose {computer_choice.upper()}...")

		# Determine the winner
		result = determine_winner(user_choice, computer_choice)
		# Print results
		print(result)

		# End the game
		if not play_again():
			print("Thanks for play Rock, Paper, Scissors with me! Bye!")
			break

# Play the game
play_game()	
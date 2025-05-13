import random
from tkinter import *

# Initialise game state variables
user_choice = None
computer_choice = None

# Get random computer choice
def get_computer_choice():
	computer_choices = ["rock", "paper", "scissors"]
	return random.choice(computer_choices)

# Get user choice
def get_user_choice():
	user_choices = {1:"rock", 2:"paper", 3:"scissors"}
	try:
		user_input = int(guess_entry.get())
		return user_choices.get(user_input, None)
	except ValueError:
		return None

# Determine winner
def determine_winner():
	# Set global variables
	global user_choice, computer_choice

	if user_choice == computer_choice:
		return "It's a tie!"
	# Determine user winning
	elif (user_choice == "rock" and computer_choice == "scissors") or \
		 (user_choice == "paper" and computer_choice == "rock") or \
		 (user_choice == "scissors" and computer_choice == "paper"):
		return "Alright alright, you beat me. Congratulations, winner."
	else:
		return "Ha! In your face! I win!!!"

# Set up game after getting user input
def play_game():
	# Set global variables
	global user_choice, computer_choice

	# Get user choice
	user_choice = get_user_choice()
	if user_choice is None:
		results.config(text="Invalid input. Please enter a number between 1 and 3.")
		return

	# Get computer choice
	computer_choice = get_computer_choice()

	# Ouptut summary
	summary = f"You chose {user_choice.upper()} and the I chose {computer_choice.upper()}..."
	results.config(text=summary)

	# Determine the winner
	result = determine_winner()
	# Print results
	results.config(text=summary + "\n\n" + result)

	# Disable the Submit button
	submit_button.config(state=DISABLED)
	# Enable the Play Again button
	play_again_button.pack()

# Reset the game
def reset_game():
	# Delete result label
	results.config(text="")
	# Clear entry box
	guess_entry.delete(0, END)
	# Set submit button back to normal
	submit_button.config(state=NORMAL)
	# Hide Play Again button
	play_again_button.pack_forget()

# Set up the GUI
def setup_gui():
	# Make all widgets global
	global results, guess_entry, submit_button, play_again_button
	# Create the window
	root = Tk()
	# Add a title
	root.title("Rock Paper Scissors Game")
	# Set up the size
	root.geometry('500x400')

	# Create label
	instructions = Label(root, text="Enter number 1, 2 or 3:" + "\n" + "1. Rock" + "\n" + " 2. Paper" + "\n" + "3. Scissors", font=("Georgia", 16))
	instructions.pack(pady=20)

	# Create entry box
	guess_entry = Entry(root, font=("Georgia", 18))
	guess_entry.pack(pady=10)

	# Create second label
	results = Label(root, text="")
	results.pack(pady=20)

	# Create buttons
	submit_button = Button(root, text="Submit Response", command=play_game)
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?", command=reset_game)
	play_again_button.pack()
	# Hide button
	play_again_button.pack_forget()

	# Start the app
	root.mainloop()

# Call main function
setup_gui()
# Import tkinter
from tkinter import *
# Import the os module/library
import os
# Import the random library
import random

# Initialise game state variables
num_to_guess = None
num_guesses = 0

# Create play_again function
def reset_game():
	# Set global variables
	global num_to_guess, num_guesses
	# Generate a random number and assign it to a variable
	num_to_guess = random.randint(1, 10)
	# Set number of guesses to 0
	num_guesses = 0
	# Delete result label
	results.config(text="")
	# Clear the entry box
	guess_entry.delete(0, END)
	# Set submit button back to normal
	submit_button.config(state=NORMAL)
	# Hide the Play Again button again
	play_again_button.pack_forget()

# Create main game function
def check_guess():
	global num_guesses
	
	# Try/except block
	try:
		guess = int(guess_entry.get())
		num_guesses += 1
		# Create some logic to check the guess
		if guess < num_to_guess:
			results.config(text="Your number is too low! Try guessing higher.")

		elif guess > num_to_guess:
			results.config(text="Your number is too high! Try guessing lower.")
			
		else:
			results.config(text=f"You guessed it! The correct number is {num_to_guess}.")
			results.config(text=f"It took you {num_guesses} guesses to get it!")
			# Disable the Guess button
			submit_button.config(state=DISABLED)
			# Enable the Play Again button
			play_again_button.pack()

	except ValueError:
		results.config(test="You did not enter a number! Game over.")

def setup_gui():
	# Make all widgets global
	global results, guess_entry, submit_button, play_again_button
	#Create the window
	root = Tk()
	# Add a title
	root.title("Guessing Game")
	# Set the size of the app
	root.geometry('500x350')

	# Create label
	instructions = Label(root, text="Guess a number between 1 and 10", font=("Georgia", 18))
	instructions.pack(pady=20)

	# Create entry box
	guess_entry = Entry(root, font=("Georgia", 18))
	guess_entry.pack(pady=10)

	# create second label
	results = Label(root, text="")
	results.pack(pady=20)

	# Create buttons
	submit_button = Button(root, text="Submit Guess", command=check_guess)
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?", command=reset_game)
	play_again_button.pack()
	# Hide button
	play_again_button.pack_forget()


	# On game start, reset game
	reset_game()

	# Start the app
	root.mainloop()

# Call main function
setup_gui()
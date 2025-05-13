# Import the os module/library
import os
# Import the random library
import random

# Create play_again function
def play_again():
	# Prompt user
	again = input("Would you like to play again? Y/N: ").upper()
	# Logic based on user response
	if again == "Y" or again == "YES":
		game()
	else:
		print("Thanks for playing my guessing game!")
		return
		
# Create main game function
def game():

	# Create variable to keep track of number of guesses
	num_guesses = 0
	correct = False

	# Clear the screen
	os.system("clear")

	# Generate a random number and assign it to a variable
	num_to_guess = random.randint(1, 10)

	# Get user input
	print("Guess a number between 1 and 10")

	# Create guessing loop
	while correct == False:
		# Try/except block
		try:
			guess = int(input("Enter your guess: "))
			print(f"You guessed the number: {guess}")
		except Exception as e:
			print("You did not enter a number! Game over.")
			return

		# Create some logic to check the guess
		if guess < num_to_guess:
			print("Your number is too low! Try guessing higher.")
			# Increment the number of guesses
			num_guesses += 1
		elif guess > num_to_guess:
			print("Your number is too high! Try guessing lower.")
			# Increment the number of guesses
			num_guesses += 1
		elif guess == num_to_guess:
			# Increment the number of guesses
			num_guesses += 1

			print(f"You guessed it! The correct number is {num_to_guess}.")
			print(f"It took you {num_guesses} guesses to get it!")
			# Set correct to True
			correct = True
			# Provide option for user to play again

			play_again()

game()
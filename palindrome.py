import os

# Clear the screen
os.system("clear")

def is_palindrome(string):
	# Remove spaces and convert to lowercase and strip notation
	'''
	new_string = ''
	# Loop through user input
	for char in string:
		# Check to see if the char is a character
		if char.isalnum():
			new_string += char.lower()
	'''
	# Shorthand version:
	new_string = ''.join(char.lower() for char in string if char.isalnum())

	# Check if the string is the same forwards nd backwards
	return new_string == new_string[::-1]

# Ask the user for input
user_input = input("Enter a word or phrase to check if it's a palindrome: ")

# Slice = [start:end:step]
# user_input = user_input[::-1]

if is_palindrome(user_input):
	print(f"'{user_input}' is a palindrome.")
else:
	print(f"'{user_input}' is NOT a palindrome.")
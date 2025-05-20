import string
import os

# Clear the screen
os.system("clear")

# Print out the password rules
def show_password_rules():
	print("Password rules: ")
	print("1. Must be at least 8 characters long.")
	print("2. Must contain at least one digit (0-9)")
	print("3. Must contain at least one lowercase letter (a-z)")
	print("4. Must contain at least one uppercase letter (A-Z)")
	print("5. Must contain at least one special character (!, @, #, $. etc.)")
	print()

def validate_password(password):
	# Check password rules
	if len(password) < 8:
		return False, "Password must be at least 8 characters long."
	# Check for digitd
	if not any(char.isdigit() for char in password):
		return False, "Password must contain at least one digit."
	# Check for lowercase
	if not any(char.islower() for char in password):
		return False, "Must contain at least one lowercase letter."
	# Check for lowercase
	if not any(char.isupper() for char in password):
		return False, "Must contain at least one uppercase letter."
	# Check for special characters
	if not any(char in string.punctuation for char in password):
		return False, "Password must contain at least one special character."
	else:
		return True, "You have created a strong password."

def password_validator():
	# Show the password rules
	show_password_rules()

	# Prompt user for their password
	password = input("Please enter your password: ")

	# Validate user password
	is_valid, message = validate_password(password)

	if is_valid:
		print("Success: ", message)
	else:
		print("Validation Failed: ", message)

# Run the program
password_validator()

from tkinter import *

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

def main():
	# Ask the user for input
	user_input = string_entry.get()

	# Slice = [start:end:step]
	# user_input = user_input[::-1]

	if is_palindrome(user_input):
		results.config(text=f"'{user_input}' is a palindrome.")
	else:
		results.config(text=f"'{user_input}' is NOT a palindrome.")

	# Disable the submit button
	submit_button.config(state=DISABLED)
	new_palindrome_button.pack()

def reset():
	results.config(text="")
	string_entry.delete(0,END)
	submit_button.config(state=NORMAL)
	new_palindrome_button.pack_forget()


def setup_gui():
	global results, string_entry, submit_button, new_palindrome_button

	root = Tk()
	root.title("Palindrome Checker")
	root.geometry('500x350')

	instructions = Label(root, text="Enter a word or phrase to check if it's a palindrome: ", font=("Courier", 16), wraplength=450)
	instructions.pack(pady=20)

	string_entry = Entry(root, font=("Courier", 14))
	string_entry.pack(pady=10)

	submit_button = Button(root, text="Submit", command=main)
	submit_button.pack(pady=20)

	new_palindrome_button = Button(root, text="Check New Palindrome", command=reset)
	new_palindrome_button.pack()
	new_palindrome_button.pack_forget()

	results = Label(root, text="", font=("Courier", 14), wraplength=450)
	results.pack(pady=20)

	root.mainloop()

setup_gui()
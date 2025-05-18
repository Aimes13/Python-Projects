from pynput import keyboard
import os

# Clear the screen
os.system("clear")

def on_press(key):
	try:
		# Check for q key
		if key.char == 'q':
			print("Exiting the program...")
			return False # Stop listener
	except AttributeError:
		pass

	# Check for arrow keys
	if key == keyboard.Key.up:
		print("You pressed the UP key!")
	elif key == keyboard.Key.down:
		print("You pressed the DOWN key!")
	elif key == keyboard.Key.left:
		print("You pressed the LEFT key!")
	elif key == keyboard.Key.right:
		print("You pressed the RIGHT key!")
	elif key == keyboard.Key.space:
		print("You pressed the SPACE key!")
	elif key == keyboard.Key.enter:
		print("You pressed the ENTER key!")
# Prompt user
print("Press arrows keys! Press 'q' to exit.")

# Create and start keyboard listener
with keyboard.Listener(on_press=on_press) as listener: # Create listener object that listens for keyboard events
	# Start the listener and wait for it to finish
	listener.join()
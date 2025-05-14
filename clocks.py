import time
from datetime import datetime
import os
import threading
from zoneinfo import ZoneInfo
# pip install tzdata

# Clear screen
def clear_screen():
	os.system("clear")

# Wait for user to hit Enter
def input_thread(stop_event):
	input()
	stop_event.set()

def main():
	# Set up time zones
	time_zones = {
	'1': ('Eastern Time', 'America/New_York'),
	'2': ('Central Time', 'America/Chicago'),
	'3': ('Pacific Time', 'America/Los_Angeles')
	}

	# Prompt user to select time zone
	print("Select your time zone: ")
	# Loop throught time zone dictionary
	for key, (name, _) in time_zones.items():
		print(f"{key}. {name}")

	# Assign user selection to variable
	user_choice = input("Enter the number of your choice: ").strip()

	# Error handling
	if user_choice not in time_zones:
		print("Invalid choice. Defaulting to Pacific Time.")
		tz_name = "America/Los_Angeles"
		tz_display_name = "Pacific Time"
	else:
		tz_display_name, tz_name = time_zones[user_choice]

	# Create event to signal when to stop clock
	stop_event = threading.Event()

	# Start input thread
	thread = threading.Thread(target=input_thread, args=(stop_event, ))
	thread.daemon = True
	thread.start()

	# Loop to update time in seconds until Enter is pressed
	while not stop_event.is_set():
		clear_screen()
		# Print current time
		#current_time = time.strftime("%H:%M:%S")
		current_time = datetime.now(ZoneInfo(tz_name)).strftime("%H:%M:%S")
		print(f"The current time is: {current_time} in {tz_display_name}.")
		# Prompt user to stop the clock
		print("Press Enter to stop the clock...")
		# Run loop once per second
		time.sleep(1)

	# Print end message
	print("Clock has stopped: you have stopped time!")

# Clear the screen
clear_screen()

# Call main function
main()
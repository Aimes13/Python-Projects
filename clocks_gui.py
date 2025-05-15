import time
from datetime import datetime
from zoneinfo import ZoneInfo
# pip install tzdata
from tkinter import *

# Global variables
running = False
tz_name = None
tz_display_name = None

def start_clock():
	global tz_name, tz_display_name, running

	# Set up time zones
	time_zones = {
	'1': ('Eastern Time', 'America/New_York'),
	'2': ('Central Time', 'America/Chicago'),
	'3': ('Pacific Time', 'America/Los_Angeles')
	}

	# Assign user selection to variable
	user_choice = zone_entry.get().strip()

	# Error handling
	if user_choice not in time_zones:
		tz_name = "America/Los_Angeles"
		tz_display_name = "Pacific Time"
	else:
		tz_display_name, tz_name = time_zones[user_choice]

	running = True
	update_clock()

	# Disable submit and show Stop Clock
	start_button.config(state=DISABLED)
	stop_button.pack()

def update_clock():
	if running:
		# Print current time
		current_time = datetime.now(ZoneInfo(tz_name)).strftime("%H:%M:%S")
		display = f"The current time is {current_time} in {tz_display_name}."
		results.config(text=display)
		# Update again after 1000ms/1s
		results.after(1000, update_clock)

def stop_clock():
	global running
	running = False
	# Print stop clock message
	results.config(text="Clock has stopped: you have stopped time!")
	stop_button.pack_forget()
	start_button.config(state=NORMAL)

# Setup GUI
def setup_gui():
	global results, zone_entry, start_button, stop_button

	root = Tk()
	root.title("Clock Stopper")
	root.geometry("650x400")

	instructions = Label(root, text="Select your time zone:\n1 = Eastern, 2 = Central, 3 = Pacific", font=("Courier", 16))
	instructions.pack(pady=20)

	zone_entry = Entry(root, font=("Courier", 16))
	zone_entry.pack(pady=10)

	results = Label(root, text="", font=("Courier", 16))
	results.pack(pady=20)

	start_button = Button(root, text="Start Clock", font=("Courier", 14), command=start_clock)
	start_button.pack(pady=10)

	stop_button = Button(root, text="Stop Clock", font=("Courier", 14), command=stop_clock)
	stop_button.pack(pady=10)
	stop_button.pack_forget()

	root.mainloop()

# Run app
setup_gui()
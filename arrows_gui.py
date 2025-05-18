from tkinter import *

root = Tk()
root.title("Keyboard Keys")
root.geometry('350x150')

def key_pressed(event):
	key = event.keysym
	if key == "Up":
		my_label.config(text="You pressed the UP key!")
	elif key == "Down":
		my_label.config(text="You pressed the DOWN key!")
	elif key == "Left":
		my_label.config(text="You pressed the LEFT key!")
	elif key == "Right":
		my_label.config(text="You pressed the RIGHT key!")
	elif key == "q":
		root.destroy()

my_label = Label(root, text="Press arrow keys. Press 'q' to exit...", font=("Georgia", 14), wraplength=300)
my_label.pack(pady=20)

# Focus the window
root.focus_set()

# Bind the keyboard
root.bind('<KeyPress>', key_pressed)

root.mainloop()
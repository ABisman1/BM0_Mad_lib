from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Stoplight/GUI Practice")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="Yellow", background='yellow')
green_button = Button(root, text="Green", background='green')
white_button = Button(root, text="Color of LIGHT")

text_box = Text(root, width= 50, height = 10)

#Add a label
label = Label(root, text="What color is the light!?")

# Place widgets in window (with pack function!)
red_button.grid(row=0,column=0)
yellow_button.grid(row=0,column=1)
green_button.grid(row=0,column=2)
white_button.grid(row=3,column=0)
label.grid(row=2,column=1)
text_box.grid(row=3,column=1,columnspan=2)

# Start the GUI event loop
root.mainloop()

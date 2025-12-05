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

#text_box = T = Text(root)

#Add a label
#label = Label(root, text="this is a stoplight")

# Place widgets in window (with pack function!)
red_button.grid(row=0,column=0,padx=5,pady=5)
yellow_button.grid(row=0,column=1,padx=5,pady=5)
green_button.grid(row=0,column=2,padx=5,pady=5)
#label.pack()
#text_box.pack()

# Start the GUI event loop
root.mainloop()

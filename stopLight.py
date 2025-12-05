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
#white_button = Button(root, text="Color of LIGHT")

#text_box = T = Text(root)

#Add a label
label = Label(root, text="What color is the light!?")

# Place widgets in window (with pack function!)
red_button.grid(row=0,column=1,padx=10,pady=10)
yellow_button.grid(row=0,column=2,padx=10,pady=10)
green_button.grid(row=0,column=3,padx=10,pady=10)
#white_button.pack()
label.grid(row=2,column=2,pacy=20)
#text_box.pack()

# Start the GUI event loop
root.mainloop()

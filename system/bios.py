import tkinter as tk

# Your ASCII logo goes here! Make sure each line ends with a newline character (\n)
logo = """
 /\\_/\\
( o.o )
 > ^ <   Meow! Welcome to Cat-OS!
"""

# Create the main window
window = tk.Tk()
window.title("Cat-OS BIOS") # This sets the title of the window

# Create a label to display the text
logo_label = tk.Label(window, text=logo, font=("Courier", 12), justify="left")
# The 'Courier' font makes it look more like old computer text
# '12' is the size of the font
# 'justify="left"' makes sure the text lines up nicely

# Put the label into the window
logo_label.pack(padx=20, pady=20) # Adds some space around the text

# Start the Tkinter event loop - this keeps the window open
window.mainloop()
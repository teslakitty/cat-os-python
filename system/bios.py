import tkinter as tk
import os
import subprocess

# Your cute ASCII logo!
logo = """
 /\\_/\\
( o.o )
 > ^ <   Meow! Welcome to Cat-OS!
"""

def show_logo():
    logo_window = tk.Tk() # Create a main window for the logo
    logo_window.title("Cat-OS BIOS")
    logo_label = tk.Label(logo_window, text=logo, font=("Courier", 12), justify="left")
    logo_label.pack(padx=20, pady=20)
    # After 2 seconds, run the lock screen and close the logo window
    logo_window.after(2000, lambda: run_lock_screen(logo_window))
    logo_window.mainloop() # Start the Tkinter event loop for the logo

def run_lock_screen(old_window):
    old_window.destroy() # Close the logo window
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lock_path = os.path.join(script_dir, "lock.py")
    subprocess.run(["python3", lock_path])

if __name__ == "__main__":
    show_logo()
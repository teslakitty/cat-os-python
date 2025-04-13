import tkinter as tk
import os
import subprocess

def run_home_screen(event):
    lock_window = event.widget.winfo_toplevel() # Get the top-level window
    lock_window.destroy()
    start_home()

def start_home():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    home_path = os.path.join(script_dir, "home.py")
    subprocess.run(["python3", home_path])

if __name__ == "__main__":
    lock_window = tk.Tk() # Create the main window for the lock screen
    lock_window.title("Cat-OS Lock Screen")
    lock_window.config(bg="#222222") # Very dark gray background

    # You can add some text or an image here if you like for the lock screen
    lock_label = tk.Label(lock_window, text="Press Space or Enter to continue...", fg="lightgray", bg="#222222")
    lock_label.pack(pady=20, padx=20)

    # Bind the Spacebar and Enter keys to the run_home_screen function
    lock_window.bind("<space>", run_home_screen)
    lock_window.bind("<Return>", run_home_screen) # <Return> is the Enter key

    lock_window.mainloop() # Start the Tkinter event loop for the lock screen
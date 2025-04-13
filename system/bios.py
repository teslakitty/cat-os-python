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
    logo_window = tk.Toplevel()
    logo_window.title("Cat-OS BIOS")
    logo_label = tk.Label(logo_window, text=logo, font=("Courier", 12), justify="left")
    logo_label.pack(padx=20, pady=20)
    # Keep the logo visible for a short time (e.g., 2 seconds)
    logo_window.after(2000, run_lock_screen)
    return logo_window

def run_lock_screen():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lock_path = os.path.join(script_dir, "lock.py")
    subprocess.run(["python3", lock_path])

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() # Hide the main empty window
    show_logo()
    root.mainloop()
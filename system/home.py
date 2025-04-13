import tkinter as tk
import os
import subprocess
import random

home_window = tk.Tk()
home_window.title("Cat-OS Home")
home_window.config(bg="#222222")

# Set the size of the home window (e.g., 600 pixels wide by 400 pixels tall)
home_window.geometry("600x400")

# Get the directory where home.py is located
home_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the main cat-os directory and then to the 'app' folder
apps_folder = os.path.join(home_dir, "..", "app")

def run_app(app_name):
    app_path = os.path.join(apps_folder, app_name + ".py")
    subprocess.run(["python3", app_path])

for filename in os.listdir(apps_folder):
    if filename.endswith(".py"):
        app_name = filename[:-3]
        button_color = random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'magenta'])
        if app_name.lower() == "store":
            button_color = "red"

        app_button = tk.Button(home_window, text=app_name, bg=button_color, fg="white", command=lambda name=app_name: run_app(name))
        app_button.pack(pady=5, padx=10, fill=tk.X)

# Let's add the shutdown button at the bottom
def shutdown():
    print("Cat-OS is shutting down...")  # Message in the terminal
    shutdown_window = tk.Toplevel(home_window)  # Create a new window on top
    shutdown_window.title("Shutting Down")
    shutdown_label = tk.Label(shutdown_window, text="Cat-OS is shutting down...")
    shutdown_label.pack(padx=20, pady=20)
    # Close all Tkinter windows after 2 seconds
    home_window.after(2000, home_window.destroy)
    home_window.after(2000, lambda: shutdown_window.destroy())

shutdown_button = tk.Button(home_window, text="Shutdown", bg="gray", fg="white", command=shutdown)
shutdown_button.pack(pady=10, padx=20, fill=tk.X, side=tk.BOTTOM) # Put it at the bottom

home_window.mainloop()
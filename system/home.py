import tkinter as tk
import os
import subprocess
import random

home_window = tk.Tk()
home_window.title("Cat-OS Home")
home_window.config(bg="#222222")

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

home_window.mainloop()
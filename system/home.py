import tkinter as tk
import os
import subprocess
import random

home_window = tk.Tk()
home_window.title("Cat-OS Home")
home_window.config(bg="#222222")

apps_folder = "app"  # Assuming your apps are in a folder named "app"

def run_app(app_name):
    app_path = os.path.join(apps_folder, app_name + ".py")
    subprocess.run(["python3", app_path])

for filename in os.listdir(apps_folder):
    if filename.endswith(".py"):
        app_name = filename[:-3]  # Remove the ".py" extension
        button_color = random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'magenta'])
        if app_name.lower() == "store":
            button_color = "red"  # Make the App Store button red

        app_button = tk.Button(home_window, text=app_name, bg=button_color, fg="white", command=lambda name=app_name: run_app(name))
        app_button.pack(pady=5, padx=10, fill=tk.X)  # fill=tk.X makes the buttons stretch horizontally

home_window.mainloop()
import tkinter as tk
import os
import subprocess

home_window = tk.Tk()
home_window.title("Cat-OS Home")
home_window.config(bg="#222222")  # Keep the background color
home_window.geometry("600x400")

home_dir = os.path.dirname(os.path.abspath(__file__))
apps_folder = os.path.join(home_dir, "..", "app")

def run_app(app_name):
    app_path = os.path.join(apps_folder, app_name + ".py")
    subprocess.Popen(["python3", app_path])  # Use Popen instead of run

for filename in os.listdir(apps_folder):
    if filename.endswith(".py"):
        app_name = filename[:-3]
        button_color = "black"  # Set the button color to black
        app_button = tk.Button(home_window, text=app_name, bg=button_color, fg="white", command=lambda name=app_name: run_app(name))
        app_button.pack(pady=5, padx=10, fill=tk.X)

def shutdown():
    print("Cat-OS is shutting down...")
    shutdown_window = tk.Toplevel(home_window)
    shutdown_window.title("Shutting Down")
    shutdown_window.config(bg="#222222") # Keep the background color for the shutdown window
    shutdown_label = tk.Label(shutdown_window, text="Cat-OS is shutting down...", bg="#222222", fg="white") # Keep label background and set text to white
    shutdown_label.pack(padx=20, pady=20)
    home_window.after(2000, home_window.destroy)
    home_window.after(2000, lambda: shutdown_window.destroy())

shutdown_button = tk.Button(home_window, text="Shutdown", bg="black", fg="white", command=shutdown) # Set shutdown button to black
shutdown_button.pack(pady=10, padx=20, fill=tk.X, side=tk.BOTTOM)

home_window.mainloop()
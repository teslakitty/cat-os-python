import tkinter as tk
import time
import os
import subprocess

# Your cute ASCII logo!
logo = """
 /\\_/\\
( o.o )
 > ^ <   Meow! Welcome to Cat-OS BIOS!
"""

def show_logo():
    logo_window = tk.Toplevel()
    logo_window.title("Cat-OS BIOS")
    logo_label = tk.Label(logo_window, text=logo, font=("Courier", 12), justify="left")
    logo_label.pack(padx=20, pady=20)
    # Keep the logo visible for a short time (e.g., 2 seconds)
    logo_window.after(2000, logo_window.destroy)
    return logo_window

def show_progress():
    progress_window = tk.Toplevel()
    progress_window.title("Loading Cat-OS")
    progress_canvas = tk.Canvas(progress_window, width=200, height=50, bg="white")
    progress_canvas.pack(padx=20, pady=20)

    paw_outline = [(20, 30), (30, 20), (50, 20), (60, 30), (60, 40), (50, 50), (30, 50), (20, 40)]
    paw = progress_canvas.create_polygon(paw_outline, outline="black", fill="#f0f0f0")
    claws = [(35, 15), (50, 15), (65, 15)]
    for claw in claws:
        progress_canvas.create_line(claw[0], claw[1], claw[0], claw[1] + 10)

    fill_width = 0
    total_steps = 100
    fill_increment = 200 / total_steps

    for i in range(total_steps + 1):
        progress_canvas.coords(paw, [(20 + fill_width, 30), (30 + fill_width, 20), (50 + fill_width, 20), (60 + fill_width, 30), (60 + fill_width, 40), (50 + fill_width, 50), (30 + fill_width, 50), (20 + fill_width, 40)])
        fill_width += fill_increment
        progress_canvas.update()
        time.sleep(0.02) # Adjusted speed

    progress_window.destroy()
    print("Cat-OS loading complete! (home.py would start here)")
    # In the future, you'd uncomment this to actually run home.py:
    # start_home()

def start_home():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    home_path = os.path.join(script_dir, "home.py")
    subprocess.run(["python3", home_path])

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() # Hide the main empty window
    show_logo()
    root.after(2500, show_progress) # Wait a bit after the logo before showing progress
    root.mainloop()
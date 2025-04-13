import tkinter as tk
from tkinter import filedialog
import os
import shutil

def install_third_party_app():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select a Python App to Install",
        filetypes=(("Python files", "*.py"), ("All files", "*.*"))
    )

    if file_path:
        app_name = os.path.basename(file_path)
        destination_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app", app_name)
        try:
            shutil.copy2(file_path, destination_path)  # Copy the file, keeping metadata
            print(f"Installed '{app_name}' in the app folder!")
            tk.messagebox.showinfo("Installation Successful", f"'{app_name}' has been installed!")
        except Exception as e:
            print(f"Error installing '{app_name}': {e}")
            tk.messagebox.showerror("Installation Failed", f"Could not install '{app_name}'. Error: {e}")

if __name__ == "__main__":
    install_third_party_app()
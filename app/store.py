import tkinter as tk
import os
import shutil

class AppStore:
    def __init__(self, master):
        self.master = master
        master.title("Cat-OS App Store")
        master.config(bg="#333333")
        self.available_apps = ["Calculator", "TextEditor", "DrawingTool", "CoolGame"]
        self.app_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app") # Path to your 'app' folder
        self.installed_apps = self.get_installed_apps()
        self.app_files = {
            "Calculator": "calculator_app.py",  # Replace with actual filenames if you have them
            "TextEditor": "text_editor.py",
            "DrawingTool": "drawing_tool.py",
            "CoolGame": "cool_game.py",
        }
        self.create_ui()

    def create_ui(self):
        tk.Label(self.master, text="Available Apps:", bg="#333333", fg="white").pack(pady=10)
        for app in self.available_apps:
            button_text = f"Install {app}" if app not in self.installed_apps else f"Uninstall {app}"
            command = lambda a=app: self.install_uninstall_app(a)
            tk.Button(self.master, text=button_text, command=command).pack(pady=5, padx=10, fill=tk.X)

    def get_installed_apps(self):
        installed = []
        if os.path.exists(self.app_folder):
            for filename in os.listdir(self.app_folder):
                if filename.endswith(".py"):
                    installed.append(filename[:-3])  # Remove .py extension
        return installed

    def install_uninstall_app(self, app_name):
        filename = self.app_files.get(app_name)
        if not filename:
            print(f"Error: Filename for {app_name} not found.")
            return

        source_path = os.path.join("available_apps", filename) # Assuming you have an 'available_apps' folder with the .py files
        dest_path = os.path.join(self.app_folder, filename)

        if app_name in self.installed_apps:
            try:
                os.remove(dest_path)
                self.installed_apps.remove(app_name)
                print(f"Uninstalled {app_name}")
            except FileNotFoundError:
                print(f"Error: {app_name} not found in the app folder.")
        else:
            # For this basic version, we'll just create an empty file to simulate installation
            try:
                with open(dest_path, 'w') as f:
                    f.write("# This is a placeholder app file.")
                self.installed_apps.append(app_name)
                print(f"Installed {app_name}")
            except Exception as e:
                print(f"Error installing {app_name}: {e}")

        # Update the button text after install/uninstall
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text").endswith(app_name):
                if app_name in self.installed_apps:
                    widget.config(text=f"Uninstall {app_name}")
                else:
                    widget.config(text=f"Install {app_name}")

def main():
    root = tk.Tk()
    app_store = AppStore(root)
    root.mainloop()

if __name__ == "__main__":
    main()
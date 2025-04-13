import tkinter as tk

class StorageManager:
    def __init__(self, master):
        self.master = master
        master.title("Cat-OS Storage Manager")
        master.config(bg="#333333")
        tk.Label(master, text="Storage Information:", bg="#333333", fg="white").pack(pady=10)
        tk.Label(master, text="Total Space: [Not Yet Detected]", bg="#333333", fg="lightgray").pack(pady=5)
        tk.Label(master, text="Used Space: [Not Yet Detected]", bg="#333333", fg="lightgray").pack(pady=5)
        tk.Label(master, text="Free Space: [Not Yet Detected]", bg="#333333", fg="lightgray").pack(pady=5)
        tk.Label(master, text="[More detailed info could go here later]", bg="#333333", fg="gray").pack(pady=15)

def main():
    root = tk.Tk()
    storage_manager = StorageManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
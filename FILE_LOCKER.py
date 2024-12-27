import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Password for the locker
LOCKER_PASSWORD = "0192837465"


def lock_file(filepath):
    """Simulate locking a file by renaming it."""
    os.rename(filepath, filepath + ".locked")


def unlock_file(filepath):
    """Simulate unlocking a file by renaming it back."""
    if filepath.endswith(".locked"):
        os.rename(filepath, filepath[:-7])


def lock_or_unlock(action):
    """Handle lock/unlock actions."""
    filepath = filedialog.askopenfilename(title="Select File")
    if not filepath:
        return

    try:
        if action == "lock":
            lock_file(filepath)
            messagebox.showinfo(
                "Success", f"File locked successfully: {filepath}")
        elif action == "unlock":
            if not filepath.endswith(".locked"):
                messagebox.showerror("Error", "Selected file is not locked!")
                return
            unlock_file(filepath)
            messagebox.showinfo(
                "Success", f"File unlocked successfully: {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Operation failed: {str(e)}")


def check_password():
    if password_entry.get() == LOCKER_PASSWORD:
        password_window.destroy()
        file_locker_options()
    else:
        messagebox.showerror("Error", "Incorrect password!")


def file_locker_options():
    options_window = tk.Tk()
    options_window.title("File Locker Options")
    options_window.geometry("400x200")

    tk.Label(options_window, text="File Locker Options",
             font=("Arial", 16)).pack(pady=10)

    tk.Button(options_window, text="Lock File", width=20,
              command=lambda: lock_or_unlock("lock")).pack(pady=5)
    tk.Button(options_window, text="Unlock File", width=20,
              command=lambda: lock_or_unlock("unlock")).pack(pady=5)

    tk.Button(options_window, text="Exit", width=20,
              command=options_window.quit).pack(pady=5)

    options_window.mainloop()


def file_locker_app():
    global password_window, password_entry
    password_window = tk.Tk()
    password_window.title("File Locker - Password")
    password_window.geometry("400x200")

    tk.Label(password_window, text="File Locker",
             font=("Arial", 16)).pack(pady=10)

    tk.Label(password_window, text="Enter Password:").pack(pady=5)
    password_entry = tk.Entry(password_window, show="*", width=30)
    password_entry.pack(pady=5)

    tk.Button(password_window, text="Submit", width=20,
              command=check_password).pack(pady=10)

    password_window.mainloop()


if __name__ == "__main__":
    file_locker_app()

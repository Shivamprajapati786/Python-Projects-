import tkinter as tk
from tkinter import messagebox, simpledialog
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    task_listbox.insert(tk.END, task)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task first.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showwarning("Selection Error", "No task selected.")

def edit_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No task selected.")
        return
    current_task = task_listbox.get(selected[0])
    new_task = simpledialog.askstring("Edit Task", "Update your task:", initialvalue=current_task)
    if new_task:
        task_listbox.delete(selected[0])
        task_listbox.insert(selected[0], new_task)

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

task_entry = tk.Entry(root, font=("Helvetica", 14))
task_entry.pack(pady=10, padx=10, fill=tk.X)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Task", width=12, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Edit Task", width=12, command=edit_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task).grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE)
task_listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

tk.Button(root, text="Save Tasks", command=save_tasks).pack(pady=5)

load_tasks()

root.mainloop()

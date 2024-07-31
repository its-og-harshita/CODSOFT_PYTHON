import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a listbox to display tasks
listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

# Create an entry field to add new tasks
entry = tk.Entry(window, font=("Helvetica", 12))
entry.pack(pady=5)

# Create buttons to add and delete tasks
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Start the main event loop
window.mainloop()
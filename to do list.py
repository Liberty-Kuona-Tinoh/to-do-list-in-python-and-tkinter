import tkinter as tk

class TodoList:
    def __init__(self):
        self.tasks = []
        self.window = tk.Tk()
        self.window.title("To-Do List")
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.window, textvariable=self.task_var)
        self.task_entry.pack()
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.pack()
        self.task_list = tk.Listbox(self.window)
        self.task_list.pack()
        self.delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        self.window.mainloop()
        
    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_var.set("")
        
    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            task = self.task_list.get(selection[0])
            self.tasks.remove(task)
            self.task_list.delete(selection[0])
        
todo_list = TodoList()
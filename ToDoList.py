import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def update_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            return removed_task
        else:
            return None


class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.master.configure(bg="lemonchiffon3")

        self.to_do_list = ToDoList()

        self.master.geometry("600x400")  # Set initial window size

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=40, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="salmon3", fg="white")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.listbox = tk.Listbox(master, width=50, height=10, font=("Helvetica", 12), selectbackground="lightblue")
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.view_tasks()

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, font=("Helvetica", 12), bg="lightpink4", fg="white")
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, font=("Helvetica", 12), bg="palegreen4", fg="white")
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.to_do_list.add_task(task)
            self.view_tasks()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def view_tasks(self):
        self.listbox.delete(0, tk.END)
        tasks = self.to_do_list.view_tasks()
        for i, task in enumerate(tasks, start=1):
            self.listbox.insert(tk.END, f"{i}. {task}")

    def update_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            index = selected_task[0] + 1
            new_task = simpledialog.askstring("Input", f"Enter the new task for task {index}:", parent=self.master)
            if new_task:
                self.to_do_list.update_task(index, new_task)
                self.view_tasks()

    def remove_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            index = selected_task[0] + 1
            removed_task = self.to_do_list.remove_task(index)
            if removed_task:
                messagebox.showinfo("Removed", f"Task {index} - '{removed_task}' removed successfully.")
                self.view_tasks()


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

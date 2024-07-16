class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def update_task(self, index, new_task):
        if index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task index!")

    def delete_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found!")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

def main():
    personal_todo_list = ToDoList()
    work_todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            list_choice = input("Enter the list (personal/work): ")
            if list_choice == "personal":
                personal_todo_list.add_task(task)
            elif list_choice == "work":
                work_todo_list.add_task(task)
            else:
                print("Invalid list choice!")
        elif choice == "2":
            index = int(input("Enter the task index: "))
            new_task = input("Enter the new task: ")
            list_choice = input("Enter the list (personal/work): ")
            if list_choice == "personal":
                personal_todo_list.update_task(index - 1, new_task)
            elif list_choice == "work":
                work_todo_list.update_task(index - 1, new_task)
            else:
                print("Invalid list choice!")
        elif choice == "3":
            index = int(input("Enter the task index: "))
            list_choice = input("Enter the list (personal/work): ")
            if list_choice == "personal":
                personal_todo_list.delete_task(index - 1)
            elif list_choice == "work":
                work_todo_list.delete_task(index - 1)
            else:
                print("Invalid list choice!")
        elif choice == "4":
            list_choice = input("Enter the list (personal/work): ")
            if list_choice == "personal":
                personal_todo_list.display_tasks()
            elif list_choice == "work":
                work_todo_list.display_tasks()
            else:
                print("Invalid list choice!")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
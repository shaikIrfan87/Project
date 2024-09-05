class ToDoList:
    def __init__(self):
        self.tasks = []
        """Code by Irfan."""

    def add_task(self, task):
        
        """Adds a new task to the list code."""

        self.tasks.append(task)
        print("Task added:", task)

    def view_tasks(self):

        """Displays all tasks in the list code."""

        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

    def mark_complete(self, task_index):

        """Marks a task as complete code."""

        if 0 <= task_index < len(self.tasks):
            completed_task = self.tasks.pop(task_index)
            print(f"Task '{completed_task}' marked as complete.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):

        """Removes a task from the list code ."""

        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task index.")

def main():

    """Main function for the To-Do List application code ."""

    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter new task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_index = int(input("Enter task number to mark complete: ")) - 1
            todo_list.mark_complete(task_index)
        elif choice == '4':
            todo_list.view_tasks()
            task_index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
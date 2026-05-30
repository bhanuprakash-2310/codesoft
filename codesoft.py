import sys

class TodoList:
    def __init__(self):
        # Using a list to maintain order, but checking against it to ensure uniqueness
        self.tasks = []

    def add_task(self, task_name):
        """Adds a new task ensuring it is unique."""
        task_name = task_name.strip()
        if not task_name:
            print("❌ Task cannot be empty!")
            return

        # Check for uniqueness (case-insensitive)
        if any(task['name'].lower() == task_name.lower() for task in self.tasks):
            print(f"❌ Error: '{task_name}' already exists in your To-Do list. Tasks must be unique!")
        else:
            self.tasks.append({"name": task_name, "completed": False})
            print(f"✅ Task '{task_name}' added successfully.")

    def view_tasks(self):
        """Displays all tasks with their status."""
        if not self.tasks:
            print("\n📝 Your To-Do list is currently empty.")
            return

        print("\n--- YOUR TO-DO LIST ---")
        for index, task in enumerate(self.tasks, start=1):
            status = "Status: Completed" if task["completed"] else "Status: Pending"
            print(f"{index}. {task['name']} [{status}]")
        print("-----------------------")

    def update_task(self, index, new_name):
        """Updates the name of an existing task while maintaining uniqueness."""
        if not self.str_to_index_is_valid(index):
            return

        idx = int(index) - 1
        new_name = new_name.strip()

        if not new_name:
            print("❌ Task name cannot be empty!")
            return

        # Check if the new name already exists elsewhere in the list
        if any(i != idx and task['name'].lower() == new_name.lower() for i, task in enumerate(self.tasks)):
            print(f"❌ Error: '{new_name}' already exists. Cannot update to a duplicate task.")
        else:
            old_name = self.tasks[idx]['name']
            self.tasks[idx]['name'] = new_name
            print(f"🔄 Task '{old_name}' updated to '{new_name}'.")

    def toggle_status(self, index):
        """Switches task status between Pending and Completed."""
        if not self.str_to_index_is_valid(index):
            return

        idx = int(index) - 1
        self.tasks[idx]['completed'] = not self.tasks[idx]['completed']
        status = "Completed" if self.tasks[idx]['completed'] else "Pending"
        print(f"✅ Task '{self.tasks[idx]['name']}' is now marked as {status}.")

    def delete_task(self, index):
        """Removes a task from the list."""
        if not self.str_to_index_is_valid(index):
            return

        idx = int(index) - 1
        removed = self.tasks.pop(idx)
        print(f"🗑️ Task '{removed['name']}' deleted successfully.")

    def str_to_index_is_valid(self, index_str):
        """Helper method to validate user input index numbers."""
        try:
            idx = int(index_str) - 1
            if 0 <= idx < len(self.tasks):
                return True
            print("❌ Error: Invalid task number. Choose a number from the list.")
            return False
        except ValueError:
            print("❌ Error: Please enter a valid number.")
            return False


def main():
    todo = TodoList()
    
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task Name")
        print("4. Toggle Task Status (Complete/Pending)")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            name = input("Enter the new task: ")
            todo.add_task(name)
        elif choice == "3":
            todo.view_tasks()
            if todo.tasks:
                num = input("Enter the task number to update: ")
                new_name = input("Enter the new name for this task: ")
                todo.update_task(num, new_name)
        elif choice == "4":
            todo.view_tasks()
            if todo.tasks:
                num = input("Enter the task number to toggle status: ")
                todo.toggle_status(num)
        elif choice == "5":
            todo.view_tasks()
            if todo.tasks:
                num = input("Enter the task number to delete: ")
                todo.delete_task(num)
        elif choice == "6":
            print("Goodbye! Stay organized! 👋")
            sys.exit()
        else:
            print("❌ Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
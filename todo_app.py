"""
Title: Command-Line To-Do List Manager
Author: Parth Patel
Description: A modular Python application demonstrating incremental development,
             object-oriented design, input validation, and clean docstrings.
"""

import sys

class TaskManager:
    """Manages a collection of tasks with operations to add, view, and delete."""

    def __init__(self):
        """Initializes an empty list to store tasks."""
        self.tasks = []

    def add_task(self, title):
        """Adds a new task dictionary to the task list."""
        if not title.strip():
            print("[Error] Task title cannot be empty.")
            return False

        task = {"title": title.strip(), "completed": False}
        self.tasks.append(task)
        print(f"[Success] Added task: '{title}'")
        return True

    def view_tasks(self):
        """Displays all current tasks with their completion status."""
        if not self.tasks:
            print("\nYour to-do list is currently empty.")
            return

        print("\n--- Current To-Do List ---")
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['title']}")
        print("-" * 26)

    def mark_complete(self, index):
        """Marks a specific task as complete based on its list index."""
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print(f"[Success] Marked task {index} as complete.")
        else:
            print("[Error] Invalid task number.")

    def delete_task(self, index):
        """Deletes a task from the list based on its index."""
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"[Success] Removed task: '{removed['title']}'")
        else:
            print("[Error] Invalid task number.")


def main():
    """CLI interface controlling user interaction and application loop."""
    manager = TaskManager()

    while True:
        print("\n=== To-Do Manager Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            manager.view_tasks()
        elif choice == '2':
            title = input("Enter task description: ")
            manager.add_task(title)
        elif choice == '3':
            manager.view_tasks()
            try:
                idx = int(input("Enter task number to mark complete: "))
                manager.mark_complete(idx)
            except ValueError:
                print("[Error] Please enter a valid integer.")
        elif choice == '4':
            manager.view_tasks()
            try:
                idx = int(input("Enter task number to delete: "))
                manager.delete_task(idx)
            except ValueError:
                print("[Error] Please enter a valid integer.")
        elif choice == '5':
            print("Exiting application. Goodbye!")
            sys.exit(0)
        else:
            print("[Error] Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
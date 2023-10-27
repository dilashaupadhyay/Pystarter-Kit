# Empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks in the to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 0 < task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please try again.")

# Main function to interact with the to-do list
def main():
    while True:
        print("\nChoose an option:")
        print("1. Display Tasks")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "3":
            display_tasks()
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(task_index)
        elif choice == "4":
            print("Exiting the to-do list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

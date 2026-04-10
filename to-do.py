# File name: todo.py

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Remove task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    except (IndexError, ValueError):
        print("Invalid input!")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the app
main()
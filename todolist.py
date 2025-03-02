import os

# Function to add a task
def add_task(task_title, task_description):
    with open("tasks.txt", "a") as f:
        f.write(f"{task_title} - {task_description}\n")
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not os.path.exists("tasks.txt"):
        print("No tasks available.")
        return
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    if tasks:
        print("\nYour To-Do List:")
        for task in tasks:
            print(task.strip())
    else:
        print("No tasks available.")

# Function to update a task
def update_task(old_task, new_task):
    if not os.path.exists("tasks.txt"):
        print("No tasks available to update.")
        return
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    with open("tasks.txt", "w") as f:
        task_updated = False
        for task in tasks:
            if old_task in task:
                f.write(new_task + "\n")
                task_updated = True
            else:
                f.write(task)
        if task_updated:
            print("Task updated!")
        else:
            print("Task not found.")

# Function to delete a task
def delete_task(task_to_delete):
    if not os.path.exists("tasks.txt"):
        print("No tasks available to delete.")
        return
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    with open("tasks.txt", "w") as f:
        task_deleted = False
        for task in tasks:
            if task_to_delete not in task:
                f.write(task)
            else:
                task_deleted = True
        if task_deleted:
            print("Task deleted!")
        else:
            print("Task not found.")

# Main application loop
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            old_task = input("Enter the task to update (part of the task title/description): ")
            new_task = input("Enter the new task details: ")
            update_task(old_task, new_task)
        elif choice == "4":
            task = input("Enter task to delete (part of the task title/description): ")
            delete_task(task)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()

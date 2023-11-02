import os

# Initialize an empty list to store tasks
tasks = []

# Function to display the list of tasks
def display_tasks():
    if not tasks:
        print("No tasks in your organizer.")
    else:
        print("Tasks in your organizer:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the organizer.")

# Function to delete a task by its index
def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted from the organizer.")
    else:
        print("Invalid task index. No task deleted.")

# Main organizer loop
while True:
    print("\nOrganizer Menu:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == '3':
        display_tasks()
        index = int(input("Enter the index of the task you want to delete: "))
        delete_task(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Optionally, you can save the tasks to a file for persistence
with open("organizer_tasks.txt", "w") as file:
    for task in tasks:
        file.write(f"{task}\n")

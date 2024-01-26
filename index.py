tasks = []
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")
def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")
def mark_completed():
    view_tasks()
    index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")
def delete_task():
    view_tasks()
    index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()

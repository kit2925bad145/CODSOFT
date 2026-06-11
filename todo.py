tasks = []

while True:
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} [{status}]")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} [{status}]")

            num = int(input("Enter task number to mark as completed: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} [{status}]")

            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                deleted_task = tasks.pop(num - 1)
                print(f"Task '{deleted_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        num = int(input("\nEnter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!")
    except:
        print("Invalid number")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

tasks = []


try:
    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f]
except FileNotFoundError:
    tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks found!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")
        print(f"Task '{task}' added")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                with open("tasks.txt", "w") as f:
                    
                    for t in tasks:
                        f.write(t + "\n")
                print(f"Task '{removed}' removed")
            except (ValueError, IndexError):
                print("Invalid choice!")

    elif choice == "4":
        print("Goodbye...")
        break
    else:
        print("Invalid input! Enter 1-4.")


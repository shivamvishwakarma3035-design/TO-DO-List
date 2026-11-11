# =====================================
# TO-DO LIST APPLICATION
# =====================================

# Task list
tasks = []

# File name
FILE_NAME = "todo.txt"


# 1. Save tasks into file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(
                f"{task['title']}|{task['status']}\n"
            )


# 2. Load tasks from file
def load_tasks():
    global tasks

    try:
        with open(FILE_NAME, "r") as file:
            tasks = []

            for line in file:
                line = line.strip()

                if "|" in line:
                    title, status = line.split("|", 1)

                    if title.strip() and status in ["Pending", "Done"]:
                        tasks.append({
                            "title": title,
                            "status": status
                        })

    except FileNotFoundError:
        tasks = []


# 3. Add a new task
def add_task():
    title = input("Enter task title: ").strip()

    if title == "":
        print("Task title cannot be empty.")
        return

    tasks.append({
        "title": title,
        "status": "Pending"
    })

    save_tasks()

    print(f"Task added. {len(tasks)} | {title} | Pending")


# 4. View all tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found. Your to-do list is empty.")
        return

    print("\n----- YOUR TASKS -----")

    for i, task in enumerate(tasks, start=1):
        print(f"{i} | {task['title']} | {task['status']}")


# 5. Complete a task
def complete_task():
    if len(tasks) == 0:
        print("No tasks found. Your to-do list is empty.")
        return

    try:
        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            print(f"Task number {number} not found.")
            return

        tasks[number - 1]["status"] = "Done"

        save_tasks()

        print(f"Task {number} marked as completed.")

    except ValueError:
        print("Invalid task number.")


# 6. Delete a task
def delete_task():
    if len(tasks) == 0:
        print("No tasks found. Your to-do list is empty.")
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print(f"Task number {number} not found.")
            return

        deleted_task = tasks.pop(number - 1)

        save_tasks()

        print(f"Task {number} deleted. Tasks left: {len(tasks)}")

    except ValueError:
        print("Invalid task number.")


# 7. Main menu
def main():
    load_tasks()

    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            save_tasks()
            print("Thank you for using To-Do List Application!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# Run application
if __name__ == "__main__":
    main()
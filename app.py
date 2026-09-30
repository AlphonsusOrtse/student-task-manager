import json
import os


DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")

    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f'{task["id"]}. [{status}] {task["title"]}')


def add_task(tasks):
    title = input("\nEnter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    new_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def complete_task(tasks):
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed.")
            else:
                task["completed"] = True
                save_tasks(tasks)
                print("Task completed successfully.")
            return

    print("Task not found.")


def delete_task(tasks):
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    print("Task not found.")


def display_menu():
    print("\n===== Student Task Manager =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        display_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
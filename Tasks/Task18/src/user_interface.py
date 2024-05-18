from business_logic import TaskService
from utilities import format_date, format_string


class App:
    def __init__(self):
        self.task_service = TaskService()

    def start_application(self):
        ''' Start the task manager application. '''
        while True:
            choice = main_menu()

            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.exit()
                break
            else:
                print("Invalid choice. Please try again!")

    def view_tasks(self):
        ''' Displays all the tasks '''
        tasks = self.task_service.get_all_tasks()
        print()
        if len(tasks) != 0:
            for task in tasks:
                display_tasks(task)
        else:
            print("There are no tasks to view!")
            input("\nPress 'Enter' to continue....")

    def add_task(self):
        ''' Adds a task to the Task Manager '''
        title = input("Enter task title: ")
        details = input("Enter task description: ")
        print("Enter due date in format -> 'YYYY-MM-DD'")
        due_date = format_date(input("Due date: "))
        new_task = [title, details, due_date]
        self.task_service.add_task(new_task)
        print("Task added successfully!")

    def delete_task(self):
        print("Enter task title of task to remove")
        remove = input("Task title: ")
        self.task_service.remove_task(remove)

    def exit(self):
        print("\nExiting the application. Goodbye!\n")


def main_menu():
    ''' Display for the main menu '''
    print("\nTask Management Application")
    print("[1] View Tasks")
    print("[2] Add Task")
    print("[3] Delete Task")
    print("[4] Quit\n")

    return input("Enter your choice: ")


def display_tasks(task):
    print("===================================")
    print(f"Title: {task[0]}\nDue date: {task[2]}")
    print("-----------------------------------")
    print(f"Description:\n{format_string(task[1])}")

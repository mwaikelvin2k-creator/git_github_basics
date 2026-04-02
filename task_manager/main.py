# Import functions from task_manager.task_utils package
from task_utils import add_task as add
from task_utils import mark_task_as_complete as mc
from task_utils import view_pending_tasks as pt
from task_utils import calculate_progress as cp


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print('please enter a valid number')
            continue
        if choice == 1:
            print('adding task')
        elif choice == 2:
            print('mark task as complete')
        elif choice == 3:
            print('pending task is: ')
        elif choice == 4:
            print('View progress')
        elif choice == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()















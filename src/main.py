class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def complete_task(self):
        self.completed= True

    def display_task(self):
        print("Title: ", self.title)
        print("Priority: ", self.priority)
        print("Completed: ", self.completed)




# priority = input("Enter a task priority: ").upper()

# if priority == "HIGH":
#     print("This task is urgent!")
# elif priority == "MEDIUM":
#     print("This task has normal priority.")
# elif priority == "LOW":
#     print("This task can wait.")
# else:
#     print("Invalid priority")

tasks = []

choice = ""

while choice != "5":
    print("\n===== PERSONAL TASK MANAGER =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title  = input("Enter the title of your task: ").strip()
        if title == "":
            print("Task title cannot be empty!")
        else:
            priority = input("Enter the priority of your task: ").upper()
            if priority in ["HIGH", "MEDIUM" , "LOW"]:
                new_task = Task(title,priority)
                tasks.append(new_task)
                print("Task added successfully!")
            else:
                print("Invalid priority. Please enter High, Medium, or Low.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for task in tasks:
                task.display_task()
                print()

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, ".", task.title)

        try:
            task_number = int(input("Enter task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1].complete_task()
                print("Task completed successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i, task in enumerate(tasks):
                print(i + 1, ".", task.title)

            try:
                task_number = int(input("Enter the number of the task you want to delete: "))
                if 1 <= task_number <= len(tasks):
                        tasks.remove(tasks[task_number - 1])
                        print("Task removed successfully!")
                else:
                        print("Invalid task number.")
            except ValueError:
                print("Invalid input.")

    
    
    elif choice == "5":
            print("Goodbye!")

    else:
        print("Invalid option. Try again.")
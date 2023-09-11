class ToDoApp:
    def __init__(self):
        self.tasks = []
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"  

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def authenticate(self, user_token):
        return user_token == self.token

    def start(self):
        print("Welcome to the To-Do List App!")
        user_token = input("Enter your authentication token: ")

        if self.authenticate(user_token):
            while True:
                print("\nMenu:")
                print("1. Add Task")
                print("2. Remove Task")
                print("3. View Tasks")
                print("4. Quit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    task = input("Enter the task: ")
                    self.add_task(task)
                    print("Task added.")
                elif choice == "2":
                    task = input("Enter the task to remove: ")
                    self.remove_task(task)
                elif choice == "3":
                    self.view_tasks()
                elif choice == "4":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Authentication failed. Exiting...")

if __name__ == "__main__":
    todo_app = ToDoApp()
    todo_app.start()

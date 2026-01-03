class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")


my_todo = TodoList()
my_todo.add_task("Python 공부")
my_todo.add_task("Git 연습")

my_todo.show_tasks()
# 출력:
# 1. Python 공부
# 2. Git 연습

my_todo.complete_task("Python 공부")
my_todo.show_tasks()
# 출력:
# 1. Git 연습
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                break

    def get_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        return pending_tasks

# Пример использования
manager = TaskManager()
manager.add_task("Купить продукты", "2024-06-22")
manager.add_task("Сделать домашнее задание", "2024-06-23")

print("Текущие задачи:")
for task in manager.get_pending_tasks():
    print(task)

manager.mark_task_completed("Купить продукты")

print("\nТекущие задачи после отметки выполненных:")
for task in manager.get_pending_tasks():
    print(task)
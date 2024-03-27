#Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
#Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    def mark_as_done(self):
        self.status = True

def add_task(tasks, description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

def list_pending_tasks(tasks):
    pending_tasks = [task for task in tasks if not task.status]
    if pending_tasks:
        print("Список текущих задач (не выполненных):")
        for i, task in enumerate(pending_tasks, 1):
            print(f"{i}. {task.description} - Срок выполнения: {task.deadline}")
    else:
        print("Нет текущих задач (все задачи выполнены)")

def mark_task_as_done(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1].mark_as_done()
        print("Задача отмечена как выполненная")
    else:
        print("Недопустимый индекс задачи")

tasks = []

add_task(tasks, "Сделать уроки по математике", "2024-04-01")
add_task(tasks, "Подготовить презентацию по Python", "2024-03-30")
add_task(tasks, "Помыть посуду", "2024-03-28")

list_pending_tasks(tasks)

mark_task_as_done(tasks, 1)

list_pending_tasks(tasks)

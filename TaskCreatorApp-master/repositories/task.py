from models.task import Task
from user import UserRepository


# Handles CRUD methods for ToDotask objects


class TaskRepository():
    @staticmethod
    def create(task, completed, task_due_date, task_goal, user_first_name):
        user = UserRepository.read(first_name=user_first_name)
        task = Task(task=task, completed=completed, task_goal=task_goal,
                    task_due_date=task_due_date, assigne=user)
        return task.put()

    @staticmethod
    def read(task_id):
        result = Task.get_by_id(int(task_id))
        return result

    @staticmethod
    def readAll():
        return Task.query().order(Task.task)

    @staticmethod
    def readAllOfUser(user_first_name):
        user = UserRepository.read(first_name=user_first_name)
        return Task.query(Task.assigne == user)

    @staticmethod
    def update(pick_task, changes):
        saved_task = TaskRepository.read(pick_task)
        if changes.task:
            saved_task.task = changes.task
        if changes.completed:
            saved_task.completed = changes.completed
        if changes.task_due_date:
            saved_task.task_due_date = changes.task_due_date
        if changes.task_goal:
            saved_task.task_goal = changes.task_goal
        if changes.assigne:
            assigne = UserRepository.read(assigne.first_name=user_first_name)
            saved_task.assigne = changes.assigne
        return saved_task.put()

    @staticmethod
    def delete(title):
        saved_task = TaskRepository.read(task)
        saved_task.delete()

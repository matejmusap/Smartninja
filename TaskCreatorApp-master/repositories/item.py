from models.item import Item
from user import UserRepository


# Handles CRUD methods for ToDoItem objects


class ItemRepository():
    @staticmethod
    def create(task, completed, task_due_date, task_goal, user_email):
        user = UserRepository.read(email=user_email)
        task = Item(task=task, completed=completed, task_goal=task_goal,
                    task_due_date=task_due_date, assigne=user)
        return task.put()

    @staticmethod
    def read(task_id):
        result = Item.get_by_id(int(task_id))
        return result

    @staticmethod
    def readAll():
        return Item.query().order(Item.task)

    @staticmethod
    def readAllOfUser(user_email):
        user = UserRepository.read(email=user_email)
        return Item.query(Item.assigne == user)

    @staticmethod
    def update(task, changes):
        saved_task = ItemRepository.read(task)
        if changes.completed:
            saved_task.completed = changes.completed
        if changes.task_due_date:
            saved_task.task_due_date = changes.task_due_date
        if changes.description:
            saved_task.task_goal = changes.task_goal
        return saved_task.put()

    @staticmethod
    def delete(title):
        saved_task = ItemRepository.read(task)
        saved_task.delete()

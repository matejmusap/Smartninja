from base import BaseHandler
from repositories.task import TaskRepository
from models.task import Task
from datetime import date
import time

# Controller that handles actions regarding tasks (to-do tasks in our app)

class TaskController(BaseHandler):
    def get(self):
        existing_tasks = TaskRepository.readAll()
        return self.render_template("/task/task_list.html", params={"taskList": existing_tasks})

    # custom method - used to handle specific user data
    def get_task(self, task_id=None):
        existing_tasks = TaskRepository.read(task_id)
        return self.render_template("/task/task_display.html", params={"task": existing_tasks})

    # custom method - handles GET request for user creation
    def create_get(self):
        return self.render_template("/task/task_create.html")

    # custom method - handles POST request for user creation
    def create_post(self):
        task = self.request.get("task")
        task_goal = self.request.get("task_goal")
        user = self.request.get("user")
        completed = False
        form_date = self.request.get("task_due_date").split('-')
        task_due_date = date(int(form_date[0]), int(
            form_date[1]), int(form_date[2]))
        new_task = TaskRepository.create(
            completed=completed, user_first_name=user, task=task, task_goal=task_goal, task_due_date=task_due_date)
        # adding lag for local development
        time.sleep(1)
        return self.redirect_to('task-list')

    def get_update_task(self, task_id=None):
        existing_tasks = TaskRepository.read(task_id)
        return self.render_template("/task/task_edit.html", params={"task": existing_tasks})

    def update_task(self, task_id=None):
        task = self.request.get("task")
        task_goal = self.request.get("task_goal")
        user = self.request.get("user")
        completed = False
        form_date = self.request.get("task_due_date").split('-')
        task_due_date = date(int(form_date[0]), int(
            form_date[1]), int(form_date[2]))
        changes = Task(completed=completed, user_first_name=user, task=task, task_goal=task_goal, task_due_date=task_due_date)
        picked_task = TaskRepository.read(task_id)
        updated_task = TaskRepository.update(picked_task, changes)
        return self.redirect_to('task-list')
        

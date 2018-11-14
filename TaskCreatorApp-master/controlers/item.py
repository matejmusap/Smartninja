from base import BaseHandler
from repositories.item import ItemRepository
from datetime import date
import time

# Controller that handles actions regarding items (to-do tasks in our app)
class ItemController(BaseHandler):
    def get(self):
        existing_items = ItemRepository.readAll()
        return self.render_template("/item/item_list.html", params={"itemList": existing_items })

    # custom method - used to handle specific user data
    def get_user(self, task = None):
        existing_items = ItemRepository.read(task)
        return self.render_template("/item/item_display.html", params={ "item": existing_items})

    # custom method - handles GET request for user creation
    def create_get(self):
        return  self.render_template("/item/item_create.html")

    # custom method - handles POST request for user creation
    def create_post(self):
        task = self.request.get("task")
        task_goal = self.request.get("task_goal")
        user = self.request.get("user")
        completed = False
        form_date = self.request.get("task_due_date").split('-')
        task_due_date = date(int(form_date[0]),int(form_date[1]),int(form_date[2]))
        new_item= ItemRepository.create(completed=completed, user_email=user, task=task, task_goal=task_goal, task_due_date=task_due_date)
        # adding lag for local development
        time.sleep(1)
        return self.redirect_to('item-list')
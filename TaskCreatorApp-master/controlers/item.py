from base import BaseHandler
from repositories.item import ItemRepository
from datetime import date
import time

# Controller that handles actions regarding items (to-do tasks in our app)


class ItemController(BaseHandler):
    def get(self):
        existing_items = ItemRepository.readAll()
        return self.render_template("/item/item_list.html", params={"itemList": existing_items})

    # custom method - used to handle specific user data
    def get_task(self, task_id=None):
        existing_items = ItemRepository.read(task_id)
        return self.render_template("/item/item_display.html", params={"item": existing_items})

    # custom method - handles GET request for user creation
    def create_get(self):
        return self.render_template("/item/item_create.html")

    # custom method - handles POST request for user creation
    def create_post(self):
        task = self.request.get("task")
        task_goal = self.request.get("task_goal")
        user = self.request.get("user")
        completed = False
        form_date = self.request.get("task_due_date").split('-')
        task_due_date = date(int(form_date[0]), int(
            form_date[1]), int(form_date[2]))
        new_item = ItemRepository.create(
            completed=completed, user_first_name=user, task=task, task_goal=task_goal, task_due_date=task_due_date)
        # adding lag for local development
        time.sleep(1)
        return self.redirect_to('item-list')

    def get_update_task(self, task_id=None):
        existing_items = ItemRepository.read(task_id)
        updated_task = update(existing_items, changes)
        return self.render_template("/item/item_edit.html", params={"item": existing_items})

    def update_task(self, task_id):
        task = Item.get_by_id(int(task_id))
        params = {"task" : task}
        return self.render_template("item_edit.html", params=params)
        

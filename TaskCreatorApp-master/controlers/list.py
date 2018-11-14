# Write the ListController here

from base import BaseHandler
from repositories.list import ListRepository
from datetime import date
import time

# Controller that handles actions regarding lists (to-do tasks in our app)


class ListController(BaseHandler):
    def get(self):
        existing_lists = ListRepository.readAll()
        return self.render_template("/list/list_list.html", params={"listList": existing_lists})

    # custom method - used to handle specific user data
    def get_list(self, project=None):
        existing_lists = ListRepository.read(project)
        return self.render_template("/list/list_display.html", params={"list": existing_lists})

    # custom method - handles GET request for user creation
    def create_get(self):
        return self.render_template("/list/list_create.html")

    # custom method - handles POST request for user creation
    def create_post(self):
        project = self.request.get("project")
        project_goal = self.request.get("project_goal")
        form_date = self.request.get("due_date").split('-')
        due_date = date(int(form_date[0]), int(
            form_date[1]), int(form_date[2]))
        new_list = ListRepository.create(
            project=project, project_goal=project_goal, due_date=due_date)
        # adding lag for local development
        time.sleep(1)
        return self.redirect_to('list-list')

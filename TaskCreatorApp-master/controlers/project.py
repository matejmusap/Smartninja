# Write the projectController here

from base import BaseHandler
from repositories.project import ProjectRepository
from datetime import date
import time

# Controller that handles actions regarding projects (to-do tasks in our app)


class ProjectController(BaseHandler):
    def get(self):
        existing_projects = ProjectRepository.readAll()
        return self.render_template("/project/project_list.html", params={"projectList": existing_projects})

    # custom method - used to handle specific user data
    def get_project(self, project_id = None):
        existing_projects = ProjectRepository.read(project_id)
        return self.render_template("/project/project_display.html", params={"project": existing_projects})

    # custom method - handles GET request for user creation
    def create_get(self):
        return self.render_template("/project/project_create.html")

    # custom method - handles POST request for user creation
    def create_post(self):
        project = self.request.get("project")
        project_goal = self.request.get("project_goal")
        form_date = self.request.get("due_date").split('-')
        due_date = date(int(form_date[0]), int(
            form_date[1]), int(form_date[2]))
        new_project = ProjectRepository.create(
            project=project, project_goal=project_goal, due_date=due_date)
        # adding lag for local development
        time.sleep(1)
        return self.redirect_to('project-list')

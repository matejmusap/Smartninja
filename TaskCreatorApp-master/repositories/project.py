# Repository for projects of tasks

from models.project import Project

# Handles CRUD methods for User objects


class ProjectRepository():
    @staticmethod
    def create(project, project_goal, due_date):
        new_project = Project(project=project,
                        project_goal=project_goal, due_date=due_date)
        project_key = new_project.put()
        return project_key

    @staticmethod
    def read(project_id):
        result = Project.get_by_id(int(project_id))
        return result

    @staticmethod
    def readAll():
        return Project.query().order(Project.project)

    @staticmethod
    def update(project, changes):
        saved_project=ProjectRepository.read(project)
        if changes.project_goal:
            saved_project.project_goal=changes.project_goal
        if changes.due_date:
            saved_project.due_date=changes.due_date
        return saved_project.put()

    @staticmethod
    def delete(project):
        saved_project=ProjectRepository.read(project)
        saved_project.delete()

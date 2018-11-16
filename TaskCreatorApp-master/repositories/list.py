# Repository for lists of tasks

from models.list import List

# Handles CRUD methods for User objects


class ListRepository():
    @staticmethod
    def create(project, project_goal, due_date):
        new_list = List(project=project,
                        project_goal=project_goal, due_date=due_date)
        list_key = new_list.put()
        return list_key

    @staticmethod
    def read(project_id):
        result = List.get_by_id(int(project_id))
        return result

    @staticmethod
    def readAll():
        return List.query().order(List.project)

    @staticmethod
    def update(project, changes):
        saved_list=ListRepository.read(project)
        if changes.project_goal:
            saved_list.project_goal=changes.project_goal
        if changes.due_date:
            saved_list.due_date=changes.due_date
        return saved_list.put()

    @staticmethod
    def delete(project):
        saved_list=ListRepository.read(project)
        saved_list.delete()

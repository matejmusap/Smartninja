import webapp2
from controlers.main import MainController
from controlers.task import TaskController
from controlers.user import UserController
from controlers.project import ProjectController

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainController),



    # example with named route - this route can be later used with the redirect_to method
    webapp2.Route('/users', UserController, name="user-list"),
    # example routes with a custom defined method for handling of requests
    webapp2.Route('/user/create', handler=UserController,
                  handler_method="create_get", methods=['GET']),
    webapp2.Route('/user/create', handler=UserController,
                  handler_method="create_post", methods=['POST']),
    # example route with string parameter included in the uri and a custom method
    # specified that handles that request
    webapp2.Route('/user/<first_name>', handler=UserController,
                  handler_method="get_user", methods=['GET']),



    webapp2.Route('/projects', ProjectController, name="project-list"),
    # example routes with a custom defined method for handling of requests
    webapp2.Route('/project/create', handler=ProjectController,
                  handler_method="create_get", methods=['GET']),
    webapp2.Route('/project/create', handler=ProjectController,
                  handler_method="create_post", methods=['POST']),
    # example route with string parameter included in the uri and a custom method
    # specified that handles that request
    webapp2.Route('/project/<project_id>', handler=ProjectController,
                  handler_method="get_project", methods=['GET']),



    webapp2.Route('/tasks', TaskController, name="task-list"),
    # example routes with a custom defined method for handling of requests
    webapp2.Route('/task/create', handler=TaskController,
                  handler_method="create_get", methods=['GET']),
    webapp2.Route('/task/create', handler=TaskController,
                  handler_method="create_post", methods=['POST']),
    webapp2.Route('/task/<task_id>', handler=TaskController,
                  handler_method="get_task", methods=['GET']),
    webapp2.Route('/task/edit/<task_id>', handler=TaskController,
                  handler_method="get_update_task", methods=['GET']),
    webapp2.Route('/task/edit/<task_id>', handler=TaskController,
                  handler_method="update_task", methods=['POST']),

    # example route with string parameter included in the uri and a custom method
    # specified that handles that request

], debug=True)

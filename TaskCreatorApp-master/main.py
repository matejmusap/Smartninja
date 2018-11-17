import webapp2
from controlers.main import MainController
from controlers.item import ItemController
from controlers.user import UserController
from controlers.list import ListController

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



    webapp2.Route('/lists', ListController, name="list-list"),
    # example routes with a custom defined method for handling of requests
    webapp2.Route('/list/create', handler=ListController,
                  handler_method="create_get", methods=['GET']),
    webapp2.Route('/list/create', handler=ListController,
                  handler_method="create_post", methods=['POST']),
    # example route with string parameter included in the uri and a custom method
    # specified that handles that request
    webapp2.Route('/list/<project_id>', handler=ListController,
                  handler_method="get_list", methods=['GET']),



    webapp2.Route('/items', ItemController, name="item-list"),
    # example routes with a custom defined method for handling of requests
    webapp2.Route('/item/create', handler=ItemController,
                  handler_method="create_get", methods=['GET']),
    webapp2.Route('/item/create', handler=ItemController,
                  handler_method="create_post", methods=['POST']),
    webapp2.Route('/item/<task_id>', handler=ItemController,
                  handler_method="get_task", methods=['GET']),
    webapp2.Route('/item/edit/<task_id>', handler=ItemController,
                  handler_method="get_update_task", methods=['GET']),
    webapp2.Route('/item/edit/<task_id>', handler=ItemController,
                  handler_method="update_task", methods=['PUT']),

    # example route with string parameter included in the uri and a custom method
    # specified that handles that request

], debug=True)

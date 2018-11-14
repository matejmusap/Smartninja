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
    webapp2.Route('/user/create', handler=UserController, handler_method="create_get", methods=['GET']),
    webapp2.Route('/user/create', handler=UserController, handler_method="create_post", methods=['POST']),

    # example route with string parameter included in the uri and a custom method
    # specified that handles that request
    webapp2.Route('/user/<email>', handler=UserController, handler_method="get_user", methods=['GET']),

    webapp2.Route('/lists', ListController, name="list-list"),

    # example routes with a custom defined method for handling of requests
    webapp2.Route('/list/create', handler=ListController, handler_method="create_get", methods=['GET']),
    webapp2.Route('/list/create', handler=ListController, handler_method="create_post", methods=['POST']),

    # example route with string parameter included in the uri and a custom method
    # specified that handles that request
    webapp2.Route('/list/<project>', handler=ListController, handler_method="get_list", methods=['GET']),

    webapp2.Route('/items', ItemController, name="item-list"),

    # example routes with a custom defined method for handling of requests
    webapp2.Route('/item/create', handler=ItemController, handler_method="create_get", methods=['GET']),
    webapp2.Route('/item/create', handler=ItemController, handler_method="create_post", methods=['POST']),

    # example route with string parameter included in the uri and a custom method
    # specified that handles that request
    webapp2.Route('/item/<task>', handler=ItemController, handler_method="get_item", methods=['GET'])
], debug=True)
# ToDoList Model

from google.appengine.ext import ndb
from item import Item

# Model that represents one task in our application
class List(ndb.Model):
    project = ndb.StringProperty()
    completed = ndb.BooleanProperty()
    project_goal = ndb.TextProperty()
    due_date = ndb.DateProperty(auto_now_add = True)
    project_task = ndb.StructuredProperty(Item)

from google.appengine.ext import ndb
from user import User

# Model that represents one task in our application
class Item(ndb.Model):
    task = ndb.StringProperty()
    completed = ndb.BooleanProperty()
    task_goal = ndb.TextProperty()
    task_due_date = ndb.DateProperty(auto_now_add = True)
    assigne = ndb.StructuredProperty(User)


from google.appengine.ext import ndb
from models.category import Category

class Outcome(ndb.Model):
    category = ndb.StructuredProperty(Category)
    outcome = ndb.StringProperty()
    amount = ndb.FloatProperty(default = 0)
    time = ndb.DateProperty(auto_now_add=True)
    place = ndb.StringProperty()

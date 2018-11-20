from google.appengine.ext import ndb
from outcome import Outcome

class Category(ndb.Model):
    name = ndb.StringProperty()
    total = ndb.FloatProperty(default = 0)
    outcome = ndb.StructuredProperty(Outcome)
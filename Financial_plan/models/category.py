from google.appengine.ext import ndb

class Category(ndb.Model):
    name = ndb.StringProperty()
    total = ndb.FloatProperty(default=0)
from google.appengine.ext import ndb

class Outcome(ndb.Model):
    outcome = ndb.StringProperty()
    amount = ndb.FloatProperty(default = 0)
    time = ndb.DateProperty(auto_now_add=True)
    place = ndb.StringProperty()
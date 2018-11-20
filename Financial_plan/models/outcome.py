from google.appengine.ext import ndb

class Outcome(ndb.Model):
    name = ndb.StringProperty()
    amount = ndb.FloatProperty(default = 0)
    time_of_spending = ndb.DateProperty(auto_now_add=True)
    place_of_spending = ndb.StringProperty()
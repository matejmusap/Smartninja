from google.appengine.ext import ndb
from google.appengine.api import users

class message(ndb.Model):
    sender = ndb.StructuredProperty(users)
    reciver = ndb.StructuredProperty(users)
    time = ndb.DateTimeProperty(auto_now_add = True)
    title = ndb.StringProperty()
    content = ndb.StringProperty()
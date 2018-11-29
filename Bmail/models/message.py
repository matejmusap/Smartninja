from google.appengine.ext import ndb

class Message(ndb.Model):
    sender = ndb.StringProperty()
    receiver = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add = True)
    title = ndb.StringProperty()
    content = ndb.StringProperty()
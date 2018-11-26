from google.appengine.ext import ndb

class message(ndb.Model):
    sender = ndb.StructuredProperty(User)
    reciver = ndb.StructuredProperty(User)
    time = ndb.DateTimeProperty(auto_now_add = True)
    title = ndb.StringProerty()
    content = ndb.StringProerty()
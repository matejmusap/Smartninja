from base import BaseHandler
from models.message import Message
from google.appengine.api import users

class NewMessageHandler(BaseHandler):
    def get(self, nickname=None):
        return self.render_template("new_message.html")
    def post(self, nickname=None):
        user = users.get_current_user()
        sender = user.email()
        receiver = self.request.get("receiver")
        title = self.request.get("title")
        content = self.request.get("content")
        new_message = Message(sender=sender, receiver=receiver, title=title, content=content)
        new_message.put()
        return self.redirect_to("homepage", nickname=user.nickname())
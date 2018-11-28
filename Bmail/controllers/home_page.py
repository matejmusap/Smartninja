from base import BaseHandler
from google.appengine.api import users
from models.message import message

class HomePageHandler(BaseHandler):
    def get(self, title, nickname=None):
        user = users.get_current_user()
        message = Message.query(Message.title == title).fetch()
        return self.render_template("home_page.html", params={"user":user, "message":message})
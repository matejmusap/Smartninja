from base import BaseHandler
from models.message import Message

class HomePageHandler(BaseHandler):
    def get(self, nickname=None):
        message = Message.query().order(Message.created)
        return self.render_template("home_page.html", params={"message": message})
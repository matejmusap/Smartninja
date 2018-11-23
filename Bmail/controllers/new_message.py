from base import BaseHandler

class NewMessageHandler(BaseHandler):
    def get(self):
        return self.render_template("home_page.html")
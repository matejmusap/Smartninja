from base import BaseHandler

class LogineHandler(BaseHandler):
    def get(self):
        return self.render_template("home_page.html")
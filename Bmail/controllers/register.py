from base import BaseHandler

class RegisterHandler(BaseHandler):
    def get(self):
        return self.render_template("home_page.html")
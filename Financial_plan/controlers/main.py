from base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")
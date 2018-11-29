from base import BaseHandler

class HomePageHandler(BaseHandler):
    def get(self, nickname=None):
        return self.render_template("home_page.html", params={})
from base import BaseHandler

class CategoryNewOutcomeHandler(BaseHandler):
    def get(self):
        return self.render_template("analyze.html")
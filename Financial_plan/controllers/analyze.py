from base import BaseHandler

class AnalyzeHandler(BaseHandler):
    def get(self):
        return self.render_template("analyze.html")
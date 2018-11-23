import webapp2
from controlers.main import MainController

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainController),
], debug=True)

import webapp2
from controllers.main import MainHandler
from controllers.login import LoginHandler
from controllers.register import RegisterHandler
from controllers.new_message import NewMessageHandler
from controllers.home_page import HomePageHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/login', LoginHandler),
    webapp2.Route('/register', Registerandler),
    webapp2.Route('/new_message', NewMessageHandler),
    webapp2.Route('/user/home', HomePageHandler),
], debug=True)

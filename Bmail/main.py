import webapp2
from controllers.main import MainHandler
from controllers.new_message import NewMessageHandler
from controllers.home_page import HomePageHandler
from controllers.weather import WeatherHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/<nickname>/home', HomePageHandler, name="homepage"),
    webapp2.Route('/<nickname>/new_message', NewMessageHandler),
    webapp2.Route('/weather', WeatherHandler),
], debug=True)

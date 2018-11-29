from base import BaseHandler
from google.appengine.api import urlfetch
import json

class WeatherHandler(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Zadar,hr&units=metric&appid=a2dd316c2c82aeca870e1b0b3bee973b"
        result = urlfetch.fetch(url)
        weather_info = json.loads(result.content)
        params = {"weather_info": weather_info}
        self.render_template("weather.html", params)

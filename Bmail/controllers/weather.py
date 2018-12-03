from base import BaseHandler
from google.appengine.api import urlfetch
import json

class WeatherHandler(BaseHandler):
    def get(self):
        return self.render_template("weather.html")
    def post(self):
        city = self.request.get("city")
        country_code = self.request.get("country_code")
        if city and country_code:
            try:
                url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_code + "&units=metric&appid=a2dd316c2c82aeca870e1b0b3bee973b"
                result = urlfetch.fetch(url)
                weather_info = json.loads(result.content)
                params = {"weather_info": weather_info, "city": city, "country_code": country_code}
                return self.render_template("weather.html", params)
            except:
                message = "No city or country code in database!"
                params = {"message": message}
                return self.render_template("weather.html", params)


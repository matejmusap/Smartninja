#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class Country():
    def __init__(self, name, capital, image):
        self.name = name
        self.capital = capital
        self.image = image

    def question(self):
        return "What is capital of " + self.name + "?"

    def answer(self):
        return "Capital of " + self.name + " is " + self.capital


Rwanda = Country("Rwanda", "Kigali", "/assets/img/Kigali.jpg")
Uzbekistan = Country("Uzbekistan", "Tashkent", "/assets/img/Tashkent.jpg")
Samoa = Country("Samoa", "Apia", "/assets/img/Apia.jpg")
Bolivia = Country("Bolivia", "LaPaz", "/assets/img/LaPaz.JPG")

list_of_countries = [Rwanda, Uzbekistan, Samoa, Bolivia]


def pick_random():
    return random.choice(list_of_countries)


country = pick_random()


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class ButtonHandler(BaseHandler):
    def get(self):
        return self.render_template("button.html")


class GameHandler(BaseHandler):
    def get(self):
        question = country.question()
        params = {"question": question}
        return self.render_template("game.html", params=params)

    def post(self):
        guess = self.request.get("guess")
        question = country.question()
        if country.capital == guess:
            answer = "Correct answer!!! " + country.answer()
            image = country.image
        else:
            answer = "Wrong answer!!! " + country.answer()
            image = country.image
        params = {"answer": answer, "question": question,
                  "guess": guess, "image": image}
        return self.render_template("game.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/button', ButtonHandler),
    webapp2.Route('/game', GameHandler),
], debug=True)

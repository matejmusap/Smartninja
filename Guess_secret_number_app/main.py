#!/usr/bin/env python
import os
import jinja2
import webapp2
import guess


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


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
        hint = "Number is between 1 and 60"
        message = "Try to guess!"
        params = {"hint": hint, "message": message}
        return self.render_template("guess.html", params=params)

    def post(self):
        secret_number = 22
        attempt = int(self.request.get("attempt"))
        hint = guess.guessing_logic(attempt, secret_number)[0]
        message = guess.guessing_logic(attempt, secret_number)[1]
        params = {"attempt": attempt, "hint": hint,
                  "message": message, "secret_number": secret_number}
        return self.render_template("guess.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)

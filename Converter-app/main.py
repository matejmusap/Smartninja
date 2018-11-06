#!/usr/bin/env python
import os
import jinja2
import webapp2
import converter


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
        result_string = "0"
        params = {"result_str": result_string}
        return self.render_template("converter.html", params=params)
    def post(self):
        dist = float(self.request.get("dist"))
        unit = self.request.get("unit")
        result_string = converter.convert(dist, unit)
        params = {"result_str": result_string}
        return self.render_template("converter.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)

#!/usr/bin/env python
import webapp2
from controlers.main import MainHandler
from controlers.category_list import ListCategoryHandler
from controlers.category_show import ShowCategoryHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/troskovi', ListCategoryHandler),
    webapp2.Route('/kategorija/<name>', ShowCategoryHandler),

], debug=True)

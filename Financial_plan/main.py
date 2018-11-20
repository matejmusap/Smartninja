#!/usr/bin/env python
import webapp2
from controlers.main import MainHandler
from controlers.category_list import ListCategoryHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/troskovi', ListCategoryHandler),

], debug=True)

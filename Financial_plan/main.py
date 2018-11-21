#!/usr/bin/env python
import webapp2
from controlers.main import MainHandler
from controlers.category_list import ListCategoryHandler
from controlers.analyze import AnalyzeHandler
from controlers.category_show import ShowCategoryHandler
from controlers.new_outcome import NewOutcomeHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/troskovi', ListCategoryHandler),
    webapp2.Route('/analiza_troskova', AnalyzeHandler),
    webapp2.Route('/kategorija/<name>', ShowCategoryHandler, name="kategorija"),
    webapp2.Route('/kategorija/<name>/novi_unos', NewOutcomeHandler),
    webapp2.Route('/kategorija/<name>/novi_unos', NewOutcomeHandler, handler_method="post", methods=['POST']),
], debug=True)

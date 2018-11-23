#!/usr/bin/env python
import webapp2
from controlers.main import MainHandler
from controlers.category_list import ListCategoryHandler
from controlers.analyze import AnalyzeHandler
from controlers.category_show import ShowCategoryHandler
from controlers.new_outcome import NewOutcomeHandler
from controlers.outcome_list import OutcomeListHandler
from controlers.category_new_outcome import CategoryNewOutcomeHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/troskovi', OutcomeListHandler),
    webapp2.Route('/troskovi/novi_unos', NewOutcomeHandler),
    webapp2.Route('/kategorije', ListCategoryHandler),
    webapp2.Route('/kategorija/<name>', ShowCategoryHandler, name="kategorija"),
    webapp2.Route('/kategoija/<name>/analiza_troskova', AnalyzeHandler),
    webapp2.Route('/kategorija/<name>/novi_unos', CategoryNewOutcomeHandler),
], debug=True)

from base import BaseHandler
from models.outcome import Outcome
from models.category import Category
from datetime import date
import time

class NewOutcomeHandler(BaseHandler):
    def get(self, name):
        return self.render_template("new_outcome.html")
    def post(self, name):
        category = Category.query(Category.name == name).fetch(1)
        outcome = self.request.get("outcome")
        amount = self.request.get("amount")
        form_date = self.request.get("time").split('-')
        time = date(int(form_date[0]), int(form_date[1]), int(form_date[2]))
        place = self.request.get("place")
        new_outcome = Outcome(category=category, outcome=outcome, amount=amount, time=time, place=place)
        new_outcome.put()
        return self.redirect_to("kategorija")
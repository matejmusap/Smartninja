from base import BaseHandler
from models.outcome import Outcome
from models.category import Category
from datetime import date

class NewOutcomeHandler(BaseHandler):
    def get(self):
        list_of_category = Category.query().order(Category.name)
        return self.render_template("new_outcome.html", params= {"list_of_category": list_of_category})
    # def post(self, name):
    #     category = Category.query(Category.name == name).fetch(1)
    #     outcome = self.request.get("outcome")
    #     amount = float(self.request.get("amount"))
    #     form_date = self.request.get("time").split('-')
    #     time = date(int(form_date[0]), int(form_date[1]), int(form_date[2]))
    #     place = self.request.get("place")
    #     new_outcome = Outcome(category=category, outcome=outcome, amount=amount, time=time, place=place)
    #     new_outcome.put()
    #     return self.redirect_to("kategorija")
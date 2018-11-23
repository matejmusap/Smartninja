from base import BaseHandler
from models.outcome import Outcome

class OutcomeListHandler(BaseHandler):
    def get(self):
        outcomes = Outcome.query().order(Outcome.outcome)
        return self.render_template("outcomes_list.html", params={"list_of_outcomes": outcomes})

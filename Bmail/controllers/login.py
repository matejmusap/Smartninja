from base import BaseHandler
from google.appengine.api import users

class LoginHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            logged_in = True
            logout_url = users.create_logout_url('/user/home')

            params = {"logged_in": logged_in, "logout_url": logout_url, "user": user}
        else:
            logged_in = False
            login_url = users.create_login_url('/login')

            params = {"logged_in": logged_in, "login_url": login_url, "user": user}
        return self.render_template("login.html")

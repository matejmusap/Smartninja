# -*- coding: utf-8 -*-
from base import BaseHandler
from models.category import Category

class ShowCategoryHandler(BaseHandler):
    def get(self, name):
        category = Category.query(Category.name == name).fetch(1)
        return self.render_template("category_show.html", params={"category": category})
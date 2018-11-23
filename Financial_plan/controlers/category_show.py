# -*- coding: utf-8 -*-
from base import BaseHandler
from models.category import Category

class ShowCategoryHandler(BaseHandler):
    def get(self):
        category = Category.query().order(Category.name)
        return self.render_template("category_show.html", params={"category": category})

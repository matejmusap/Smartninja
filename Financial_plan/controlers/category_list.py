# -*- coding: utf-8 -*-
from base import BaseHandler
from models.category import Category

class ListCategoryHandler(BaseHandler):
    def get(self):
        list_of_category = Category.query().order(Category.name)
        return self.render_template("category_list.html", params= {"list_of_category": list_of_category})
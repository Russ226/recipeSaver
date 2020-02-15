from os import sys, path



sys.path.append('/home/russ/recipeApp/recipeSaver/')

import os
from flask import Flask

from WebLayer.Controllers.RecipeController import RecipeController
from WebLayer.Controllers.RecipeSearchController import RecipeSearchController


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'dude'
	app.secret_key = os.urandom(24)
	app.add_url_rule('/api/recipe/<recipeTitle>', view_func=RecipeController.as_view('recipesGet'), methods=['GET'])
	app.add_url_rule('/api/recipe/search/<recipeTitle>', view_func=RecipeSearchController.as_view('recipeSearchGet'), methods=['GET'])
	app.add_url_rule('/api/recipe/', view_func=RecipeController.as_view('recipesPost'), methods=['POST'])
	return app

app = create_app()

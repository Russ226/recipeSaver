import os
from flask import Flask

from WebLayer.Controllers.RecipeController import RecipeController


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'dude'
	app.secret_key = os.urandom(24)
	app.add_url_rule('/recipe/<recipeTitle>', view_func=RecipeController.as_view('recipesGet'), methods=['GET'])
	app.add_url_rule('/recipe/', view_func=RecipeController.as_view('recipesPost'), methods=['POST'])
	return app

app = create_app()

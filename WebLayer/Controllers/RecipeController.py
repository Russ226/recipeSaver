from flask.views import MethodView


class RecipeController(MethodView):
    def post(self):
        urlToParse = self.request.json['recipeUrl']
from flask import make_response, jsonify, request
from flask.views import MethodView
from config.Povider import Provider


class RecipeSearchController(MethodView):

    def get(self, recipeTitle):
        recipeSaverService = Provider.createRecipeSearchService()

        returnMessage = recipeSaverService.searchRecipesByTitle(recipeTitle.replace('%20', ' '))

        if returnMessage['isError']:
            return make_response(jsonify(returnMessage), 400)

        return make_response(jsonify(returnMessage), 200)





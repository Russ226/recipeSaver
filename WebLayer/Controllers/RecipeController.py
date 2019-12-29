from flask import make_response, jsonify, request
from flask.views import MethodView
from config.Povider import Provider


class RecipeController(MethodView):
    def post(self):
        urlToParse = request.json['recipeUrl']
        recipeSaverService = Provider.createRecipeSaverService()
        try:
            returnMessage = recipeSaverService.saveRecipe(urlToParse)

            if returnMessage['isError']:
                return make_response(jsonify(returnMessage), 400)

            return make_response(jsonify(returnMessage), 200)
        except Exception as e:
            return make_response(jsonify({'message': str(e)}), 500)

    def get(self, recipeTitle):
        recipeSaverService = Provider.createRecipeSaverService()

        returnMessage = recipeSaverService.getFullRecipeByTitle(recipeTitle.replace('%20', ' '))

        if returnMessage['isError']:
            return make_response(jsonify(returnMessage), 400)

        return make_response(jsonify(returnMessage), 200)





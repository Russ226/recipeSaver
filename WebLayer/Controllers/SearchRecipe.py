from flask import make_response, jsonify, request
from flask.views import MethodView
from config.Povider import Provider


class SearchRecipeController(MethodView):

    def get(self, title):
        searchService = Provider.recipeSearchService()


        try:
            result = searchService.searchRecipesByTitle(title)

            if result['isError']:
                return make_response(jsonify(result), 400)

            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'message': str(e)}), 500)
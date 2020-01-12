class RecipeSearchService:
    def __init__(self, recipeDal):
        self.recipeDal = recipeDal


    def searchRecipesByTitle(self, recipeTitle):
        returnMessage = {
            'isError': False,
            'errorMessage': '',
            'result': None
        }

        recipes = None

        try:
            recipes = self.recipeDal.searchRecipeByTitle(recipeTitle)

        except Exception as e:
            returnMessage['isError'] = True
            returnMessage['errorMessage'] = str(e)

        finally:
            returnMessage['result'] = recipes
            return returnMessage
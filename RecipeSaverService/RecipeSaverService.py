from RecipeDAL.Utilities.Exceptions.RecipeDalError import RecipeDalError


class RecipeSaveService:
    def __init__(self, recipeDAL, recipeParser):
        self.recipeDAL = recipeDAL
        self.recipeParser = recipeParser


    def saveRecipe(self, recipeSoupObj):
        returnMessage = {
            'isError': False,
            'errorMessage': '',
            'newRecipe': None
        }
        ## parse recipe page
        newRecipe = self.recipeParser.parseRecipePage(recipeSoupObj)

        ## save recipe in db

        try:
            self.recipeDAL.saveNewRecipe(newRecipe)
            returnMessage['newRecipe'] = newRecipe

            return

        except RecipeDalError as dalError:
            returnMessage['isError'] = True
            returnMessage['errorMessage'] = dalError

        finally:
            return returnMessage


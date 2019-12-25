from RecipeDAL.Utilities.Exceptions.RecipeDalError import RecipeDalError


class RecipeSaveService:
    def __init__(self, recipeSaverDAL, recipeParserFactory):
        self.recipeSaverDAL = recipeSaverDAL
        self.recipeParserFactory = recipeParserFactory


    def saveRecipe(self, recipeSoupObj):
        returnMessage = {
            'isError': False,
            'errorMessage': '',
            'newRecipe': None
        }

        ## parse recipe page
        newRecipe = self.recipeParserFactory.parseRecipePage(recipeSoupObj)

        ## save recipe in db
        try:
            self.recipeSaverDAL.saveNewRecipe(newRecipe)

        except Exception as e:
            returnMessage['isError'] = True
            returnMessage['errorMessage'] = e

        finally:
            returnMessage['newRecipe'] = newRecipe
            return returnMessage


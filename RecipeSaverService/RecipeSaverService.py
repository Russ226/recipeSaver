from RecipeDAL.Utilities.Exceptions.RecipeDalError import RecipeDalError


class RecipeSaverService:
    def __init__(self, recipeSaverDAL, recipeParserFactory, webRequestorFactory):
        self.webRequestorFactory = webRequestorFactory
        self.recipeSaverDAL = recipeSaverDAL
        self.recipeParserFactory = recipeParserFactory


    def saveRecipe(self, url):
        returnMessage = {
            'isError': False,
            'errorMessage': '',
            'newRecipe': None
        }




        try:
            ## create soup obj from url
            recipeSoupObj = self.recipeParserFactory.requestSoupPage(url)

            ## parse recipe page
            newRecipe = self.recipeParserFactory.parseRecipePage(recipeSoupObj)

            ## save recipe in db
            self.recipeSaverDAL.saveNewRecipe(newRecipe)

        except Exception as e:
            returnMessage['isError'] = True
            returnMessage['errorMessage'] = e

        finally:
            returnMessage['newRecipe'] = newRecipe
            return returnMessage


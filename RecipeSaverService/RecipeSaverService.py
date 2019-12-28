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
            'recipe': None
        }

        newRecipe = None

        try:
            ## create soup obj from url
            recipeSoupObj = self.webRequestorFactory.requestSoupPage(url)

            ## parse recipe page
            newRecipe = self.recipeParserFactory.parseRecipePage(recipeSoupObj)

            ## save recipe in db
            self.recipeSaverDAL.saveNewRecipe(newRecipe)

        except Exception as e:
            returnMessage['isError'] = True
            returnMessage['errorMessage'] = e

        finally:
            returnMessage['recipe'] = newRecipe
            return returnMessage


    def getfullRecipeById(self, id):
        returnMessage = {
            'isError': False,
            'errorMessage': '',
            'recipe': None
        }

        recipe = None
        try:
            self.recipeSaverDAL.getFullRecipeByTitle(id)

        except Exception as e:
            returnMessage['isError'] = True
            returnMessage['errorMessage'] = e

        finally:
            returnMessage['recipe'] = recipe
            return returnMessage




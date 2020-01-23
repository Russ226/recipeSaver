import pymysql.cursors

from RecipeDAL.Utilities.Exceptions.InvalidRecipeSchema import InvalidRecipeSchema
from RecipeDAL.Utilities.Exceptions.RecipeDalError import RecipeDalError
from .Utilities import StoredProcs

class RecipeDAL:
    def __init__(self, **kwargs):
        self.dbConfig = kwargs
        self.dbConfig["cursorclass"] = pymysql.cursors.DictCursor


    ## insert methods

    def saveNewRecipeGeneralInfo(self, recipe):

        sqlConnection = pymysql.connect(**self.dbConfig)
        try:



            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveRecipeProc(), (recipe.title, recipe.nutritionFacts['servingsPerRecipe'],
                                                              recipe.cookTime, recipe.prepTime, recipe.totalTime))
                sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new recipe {str(e)}')

        finally:
            sqlConnection.close()

        return


    def saveNewRecipeIngredient(self, ingredient, recipeId = None, recipeTitle = None):

        if recipeId is None and recipeTitle is None:
            raise InvalidRecipeSchema('recipeId and recipeTile cannot be None please provide one or the other')
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:


            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveIngredientProc(), (ingredient, recipeId, recipeTitle))

            sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new ingredient {str(e)}')

        finally:
            sqlConnection.close()

        return

    def saveNewRecipeDirection(self, directionStepNumber, directionText, recipeId = None, recipeTitle = None):

        if recipeId is None and recipeTitle is None:
            raise InvalidRecipeSchema('recipeId and recipeTile cannot be None please provide one or the other')
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:


            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveDirectionProc(), (directionStepNumber, directionText, recipeId, recipeTitle))

            sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new direction {str(e)}')

        finally:
            sqlConnection.close()

        return


    def saveNewRecipeNutritionFact(self, nutritionName, nutritionAmount, nutritionUnit,recipeId = None, recipeTitle = None):

        if recipeId is None and recipeTitle is None:
            raise InvalidRecipeSchema('recipeId and recipeTile cannot be None please provide one or the other')
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:


            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveNutitionProc(), (nutritionName, nutritionAmount,
                                                                nutritionUnit, recipeId, recipeTitle))

            sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new nutrition fact {str(e)}')

        finally:
            sqlConnection.close()

        return

    def saveNewRecipe(self, newRecipe):

        # save general info
        self.saveNewRecipeGeneralInfo(newRecipe)

        # save ingredients
        for ingredient in newRecipe.ingredients:
            self.saveNewRecipeIngredient(ingredient, None, newRecipe.title)

        # save directions

        for index, direction in enumerate(newRecipe.directions):
            if not direction:
                raise InvalidRecipeSchema(f'invalid direction for recipe:{newRecipe.title} ,empty direction text')
            self.saveNewRecipeDirection(index, direction, None, newRecipe.title)

        # save nutrition facts
        for nutritionName, nutritionAmount in newRecipe.nutritionFacts.items():

            if type(nutritionAmount) is list:
                self.saveNewRecipeNutritionFact(nutritionName, nutritionAmount[0], nutritionAmount[1], None, newRecipe.title)

            elif type(nutritionAmount) is str:
                self.saveNewRecipeNutritionFact(nutritionName, nutritionAmount, None, None, newRecipe.title)

            else:
                raise InvalidRecipeSchema(f'invalid nutrition for recipe:{newRecipe.title} insertion with the name {nutritionName}, must have a amount and unit instead got: [{nutritionAmount}]')

        return

    ## get methods
    def getRecipeGeneralByTitle(self, recipeTitle):

        result = None
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.getRecipeByTitleProc(), (recipeTitle))
                result = cursor.fetchone()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new recipe {str(e)}')

        finally:
            sqlConnection.close()
            return result


    def getRecipeIngredientsByRecipeId(self, recipeId):

        result = None
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.getIngredientForRecipeProc(), (recipeId))
                result = cursor.fetchall()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new recipe {str(e)}')

        finally:
            sqlConnection.close()
            return result


    def getRecipeDirectionsByRecipeId(self, recipeId):

        result = None
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.getDirectionsForRecipeProc(), (recipeId))
                result = cursor.fetchall()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new recipe {str(e)}')

        finally:
            sqlConnection.close()
            return result


    def getRecipeNutritionalFactsByRecipeId(self, recipeId):

        result = None
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.getNutritionForRecipeProc(), (recipeId))
                result = cursor.fetchall()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new recipe {str(e)}')

        finally:
            sqlConnection.close()
            return result


    def getFullRecipeByTitle(self, recipeTitle):


        recipe = self.getRecipeGeneralByTitle(recipeTitle)

        if recipe is not None:
            recipe['ingredients'] = self.getRecipeIngredientsByRecipeId(recipe['id'])

            recipe['directions'] = self.getRecipeDirectionsByRecipeId(recipe['id'])

            recipe['nutritionFacts'] = self.getRecipeNutritionalFactsByRecipeId(recipe['id'])

        return recipe


    def searchRecipeByTitle(self, recipeTitle):
        result = None
        sqlConnection = pymysql.connect(**self.dbConfig)
        try:
            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.getSearchByRecipeTitleProc(), (recipeTitle))
                result = cursor.fetchall()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new recipe {str(e)}')

        finally:
            sqlConnection.close()
            return result
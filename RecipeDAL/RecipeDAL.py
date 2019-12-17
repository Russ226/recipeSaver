import pymysql.cursors

from RecipeDAL.Utilities.Exceptions.InvalidRecipeSchema import InvalidRecipeSchema
from RecipeDAL.Utilities.Exceptions.RecipeDalError import RecipeDalError
from .Utilities import StoredProcs

class RecipeDAL:
    def __init__(self, **kwargs):
        self.dbConfig = kwargs
        self.dbConfig["cursorclass"] = pymysql.cursors.DictCursor




    def saveNewRecipeGeneralInfo(self, recipe):


        try:
            sqlConnection = pymysql.connect(**self.dbConfig)
            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveRecipeProc(), (recipe['recipeTitle'], recipe['servings'],
                                                              recipe['cookTime'], recipe['prepTime'], recipe['totalTime']))
                sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new recipe {e}')

        finally:
            sqlConnection.close()

        return


    def saveNewRecipeIngredient(self, ingredient, recipeId = None, recipeTitle = None):

        if recipeId is None and recipeTitle is None:
            raise TypeError('recipeId and recipeTile cannot be None please provide one or the other')

        try:
            sqlConnection = pymysql.connect(**self.dbConfig)

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveIngredientProc, (ingredient, recipeId, recipeTitle))

            sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new ingredient {e}')

        finally:
            sqlConnection.close()

        return

    def saveNewRecipeDirection(self, directionStepNumber, directionText, recipeId = None, recipeTitle = None):

        if recipeId is None and recipeTitle is None:
            raise TypeError('recipeId and recipeTile cannot be None please provide one or the other')

        try:
            sqlConnection = pymysql.connect(**self.dbConfig)

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveDirectionProc(), (directionStepNumber, directionText, recipeId, recipeTitle))

            sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new direction {e}')

        finally:
            sqlConnection.close()

        return


    def saveNewRecipeNutritionFact(self, nutritionName, nutritionAmount, nutritionUnit,recipeId = None, recipeTitle = None):

        if recipeId is None and recipeTitle is None:
            raise TypeError('recipeId and recipeTile cannot be None please provide one or the other')

        try:
            sqlConnection = pymysql.connect(**self.dbConfig)

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveNutitionProc(), (nutritionName, nutritionAmount,
                                                                nutritionUnit, recipeId, recipeTitle))

            sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new nutrition fact {e}')

        finally:
            sqlConnection.close()

        return

    def saveNewRecipe(self, newRecipe):

        # save general info
        self.saveNewRecipeGeneralInfo(newRecipe)

        # save ingredients
        for ingredient in newRecipe['ingredients']:
            self.saveNewRecipeIngredient(ingredient, None, newRecipe['recipeTitle'])

        # save directions

        for index, direction in enumerate(['directions']):
            if not direction:
                raise InvalidRecipeSchema(f'invalid direction for recipe:{newRecipe["recipeTitle"]} ,empty direction text')
            self.saveNewRecipeDirection(index, direction, None, newRecipe['recipeTitle'])

        # save nutrition facts
        for nutritionFact in newRecipe['nutritionFacts']:
            nutritionName = nutritionFact[nutritionFact.keys()[0]]
            if len(nutritionName) == 1:
                self.saveNewRecipeNutritionFact(nutritionFact, nutritionFact[nutritionFact][0], nutritionFact[nutritionFact][1], None, newRecipe['recipeTitle'])

            elif len(nutritionName) == 2:
                self.saveNewRecipeNutritionFact(nutritionFact, nutritionFact[nutritionFact][0], None, None, newRecipe['recipeTitle'])

            else:
                raise InvalidRecipeSchema(f'invalid nutrition for recipe:{newRecipe["recipeTitle"]} insertion with the name {nutritionName}, must have a amount and unit instead got: [{nutritionFact[nutritionFact]}]')

        return


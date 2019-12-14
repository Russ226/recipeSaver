import pymysql.cursors

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


    def saveNewRecipeNutritionFact(self, nutritionFact, recipeId = None, recipeTitle = None):

        if recipeId is None and recipeTitle is None:
            raise TypeError('recipeId and recipeTile cannot be None please provide one or the other')

        try:
            sqlConnection = pymysql.connect(**self.dbConfig)

            with sqlConnection.cursor() as cursor:
                cursor.execute(StoredProcs.saveNutitionProc(), (nutritionFact['name'], nutritionFact['amount'],
                                                                nutritionFact['unit'], recipeId, recipeTitle))

            sqlConnection.commit()

        except Exception as e:
            sqlConnection.rollback()
            raise RecipeDalError(f'an error has occured while an inserting a new nutrition fact {e}')

        finally:
            sqlConnection.close()

        return
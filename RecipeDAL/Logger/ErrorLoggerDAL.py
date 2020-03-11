import pymysql


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
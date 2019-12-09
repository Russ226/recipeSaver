import pymysql
from .Utilities import StoredProcs

class RecipeDAL:
    def __init__(self, config):
        self.sqlConnection = pymysql.connect(host=config['host'],
                                             user=config['user'],
                                             password=config['password'],
                                             db=config['db'],
                                             charset=config['charset'],
                                             cursorclass=pymysql.cursors.DictCursor
                                            )


    def saveNewRecipeGeneralInfo(self, recipe):
        with self.sqlConnection.cursor() as cursor:
            cursor.execute(StoredProcs.saveRecipeProc(), [recipe['recipeTitle'], recipe['servings'],
                                                          recipe['cookTime'], recipe['prepTime'], recipe['totalTime']])

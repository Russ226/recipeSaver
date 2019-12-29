import json
import os

import pymysql

from RecipeDAL.RecipeDAL import RecipeDAL


class DALRunner:
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'TestData/allRecipeEachParseTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testData = json.loads(testData)

        with open(os.path.join(os.path.dirname(__file__), 'TestData/DbConfig.json'), 'r') as testData:
            config = testData.read()

        self.config = json.loads(config)
        self.config["cursorclass"] = pymysql.cursors.DictCursor

def saveRecipe():
    dalRunner = DALRunner()
    recipeSaver = RecipeDAL(**dalRunner.config)

    recipeSaver.saveNewRecipe(dalRunner.testData["chocolateChipCookies"])

def getGeneralInfo():
    dalRunner = DALRunner()
    recipeSaver = RecipeDAL(**dalRunner.config)

    result = recipeSaver.getRecipeGeneralByTitle("Best Chocolate Chip Cookies")
    print(result)

def getIngredients():
    dalRunner = DALRunner()
    recipeSaver = RecipeDAL(**dalRunner.config)

    result = recipeSaver.getRecipeIngredientsByRecipeId(20)
    print(result)

def getDirections():
    dalRunner = DALRunner()
    recipeSaver = RecipeDAL(**dalRunner.config)

    result = recipeSaver.getRecipeDirectionsByRecipeId(20)
    print(result)

def getFullRecipe():
    dalRunner = DALRunner()
    recipeSaver = RecipeDAL(**dalRunner.config)

    result = recipeSaver.getFullRecipeByTitle("Best Chocolate Chip Cookies")
    print(result)


def main():
    getFullRecipe()


if __name__ == '__main__':
    main()


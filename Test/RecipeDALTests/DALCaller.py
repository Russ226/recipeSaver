import json
import os

import pymysql

from RecipeDAL.RecipeDAL import RecipeDAL


class DALRunner:
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'TestData/allRecipeEachParseTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testData = json.loads(testData)

        with open(os.path.join(os.path.dirname(__file__), 'TestData/DbTestConfig.json'), 'r') as testData:
            config = testData.read()

        self.config = json.loads(config)
        self.config["cursorclass"] = pymysql.cursors.DictCursor

def main():
    dalRunner = DALRunner()
    recipeSaver = RecipeDAL(**dalRunner.config)

    recipeSaver.saveNewRecipe(dalRunner.testData["chocolateChipCookies"])


if __name__ == '__main__':
    main()


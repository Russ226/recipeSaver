import json
import os
import unittest

import pymysql.cursors

from RecipeDAL.RecipeDAL import RecipeDAL
from RecipeDAL.Models.RecipeModel import Recipe


class RecipeDALTests(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), 'TestData/allRecipeEachParseTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testData = json.loads(testData)

        with open(os.path.join(os.path.dirname(__file__), 'TestData/DbTestConfig.json'), 'r') as testData:
            config = testData.read()

        self.config = json.loads(config)
        self.config["cursorclass"] = pymysql.cursors.DictCursor





    def test_saving_recipe_general_info(self):
        recipeSaver = RecipeDAL(**self.config)
        recipe = Recipe(self.testData["bakedChickenThighs"])
        recipeSaver.saveNewRecipeGeneralInfo(recipe)

        self.sqlConnection = pymysql.connect(**self.config)
        with self.sqlConnection.cursor() as cursor:
            cursor.execute('select * from recipes where title=%s', ( self.testData["bakedChickenThighs"]["title"]))
            self.result = cursor.fetchone()

        self.sqlConnection.close()

        self.assertTrue(self.result['title'], self.testData["bakedChickenThighs"]["title"])





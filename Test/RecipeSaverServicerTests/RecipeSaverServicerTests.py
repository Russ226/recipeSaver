import json
import os
import unittest

import pymysql.cursors

from Parser.ParserFactory import ParserFactory
from RecipeDAL.RecipeDAL import RecipeDAL
from RecipeSaverService.RecipeSaverService import RecipeSaverService


class RecipeSaverServiceTests(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), 'TestData/allRecipeEachParseTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testData = json.loads(testData)

        with open(os.path.join(os.path.dirname(__file__), 'TestData/DbTestConfig.json'), 'r') as testData:
            config = testData.read()

        self.config = json.loads(config)
        self.config["cursorclass"] = pymysql.cursors.DictCursor



    def test_savingRecipe(self):
        self.recipeDAL = RecipeDAL(**self.config)
        self.recipeParserFactory = ParserFactory()

        self.recipeSaverService = RecipeSaverService(self.recipeDAL, self.recipeParserFactory)



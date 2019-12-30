import json
import os
import unittest

import pymysql

from RecipeDAL.RecipeDAL import RecipeDAL
from RecipeSaverService.RecipeSearchService import RecipeSearchService


class RecipeSaverServiceTests(unittest.TestCase):

    def setUp(self):

        with open(os.path.join(os.path.dirname(__file__), 'TestData/DbTestConfig.json'), 'r') as testData:
            config = testData.read()

        self.config = json.loads(config)
        self.config["cursorclass"] = pymysql.cursors.DictCursor


    def test_searchingForRecipesWithChInIt(self):
        recipeDAL = RecipeDAL(**self.config)
        recipeSearchService = RecipeSearchService(recipeDAL)

        result = recipeSearchService.searchRecipesByTitle('Ch')

        self.assertEqual(result['isError'], False)
        self.assertEqual(any(title['title'] in 'Crispy and Tender Baked Chicken Thighs' for title in result['result']), True)

    def test_searchingForRecipesWithEmptyList(self):
        recipeDAL = RecipeDAL(**self.config)
        recipeSearchService = RecipeSearchService(recipeDAL)

        result = recipeSearchService.searchRecipesByTitle('xz')

        self.assertEqual(result['isError'], False)
        self.assertEqual(len(result['result']), 0)
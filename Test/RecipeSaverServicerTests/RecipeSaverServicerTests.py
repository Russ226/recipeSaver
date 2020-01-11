import json
import os
import unittest

import pymysql.cursors

from RecipeParser.src.Parser.ParserFactory import ParserFactory
from RecipeDAL.RecipeDAL import RecipeDAL
from RecipeSaverService.RecipeSaverService import RecipeSaverService
from RecipeParser.src.WebRequestor.WebRequestorFactory import WebRequestorFactory


class RecipeSaverServiceTests(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), 'TestData/allRecipeEachParseTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testData = json.loads(testData)["chocolateChipCookies"]

        with open(os.path.join(os.path.dirname(__file__), 'TestData/DbConfig.json'), 'r') as testData:
            config = testData.read()

        self.config = json.loads(config)
        self.config["cursorclass"] = pymysql.cursors.DictCursor



    def test_savingRecipe(self):
        self.recipeDAL = RecipeDAL(**self.config)
        self.recipeParserFactory = ParserFactory()
        self.webRequestorFactory = WebRequestorFactory()

        self.recipeSaverService = RecipeSaverService(self.recipeDAL, self.recipeParserFactory, self.webRequestorFactory)

        result = self.recipeSaverService.saveRecipe('https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/')
        recipe = result['newRecipe']
        self.assertTrue(result['isError'], False)


        for ing in recipe.ingredients:
            self.assertTrue(ing in self.testData["ingredients"], True)


        counter = 0
        for dire in recipe.directions:
            self.assertTrue(dire, self.testData["directions"][counter])
            counter += 1


        self.assertTrue(self.testData["recipeTitle"], recipe.title)
        self.assertTrue(self.testData["cookTime"], recipe.cookTime)
        self.assertTrue(self.testData["prepTime"], recipe.prepTime)
        self.assertTrue(self.testData["totalTime"], recipe.totalTime)

    ## needs to be fixed

        for key, amount in self.testData["nutritionFacts"].items():
            self.assertTrue(recipe.nutritionFacts[key][0], amount)

if __name__ == '__main__':
    unittest.main()



import unittest
import json
import os
from venv import logger

from bs4 import BeautifulSoup
import requests
from Parser.AllRecipeParser import AllRecipeParserOldSite

headers = {
    "user-agent": "ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36"
}


class AllRecipeOldSiteParserTests(unittest.TestCase):

    def setUp(self):
        recipeGet = requests.get('https://www.allrecipes.com/recipe/235151/crispy-and-tender-baked-chicken-thighs/', headers=headers)
        self.recipeSoup = BeautifulSoup(recipeGet.content, 'html.parser')

        with open(os.path.join(os.path.dirname(__file__),'TestData/allRecipeEachParseTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testdata = json.loads(testData)["bakedChickenThighs"]

        self.recipeParser = AllRecipeParserOldSite(self.recipeSoup)

    def test_parse_ingredients(self):

        for ing in self.recipeParser.ingredients:
            try:
                ingredientExtists= filter(ing, self.testdata["ingredients"])
                self.assertTrue(ingredientExtists, True)
            except AssertionError as err:
                logger.exception(f'My assert failed :({err}) \n ing = {ing}')
                raise err



    def test_parse_directions(self):
        counter =0
        for dire in self.recipeParser.directions:
            self.assertTrue(dire,  self.testdata["directions"][counter])
            counter+=1

    def test_general_recipe_info(self):
        self.assertTrue(self.testdata["title"], self.recipeParser.title)
        self.assertTrue(self.testdata["cookingTime"], self.recipeParser.cookTime)
        self.assertTrue(self.testdata["prepTime"], self.recipeParser.prepTime)
        self.assertTrue(self.testdata["totalTime"], self.recipeParser.totalTime)


    def test_nutrition_content(self):

        for key, amount in self.testdata["nutritionFacts"].items():
            try:
                nutritionexists = filter(key, self.recipeParser.nutritionFacts)
                self.assertTrue(nutritionexists, True)
                self.assertTrue(self.recipeParser.nutritionFacts[key][0], amount)
            except AssertionError as err:
                logger.exception(f'My assert failed :({err}) \n ing = {key} {amount}')
                raise err

if __name__ == '__main__':
    unittest.main()
import unittest
import json
import os
from bs4 import BeautifulSoup
import requests
from Parser.AllRecipeParser import AllRecipeParserNewSite

headers = {
    "user-agent": "ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36"
}


class AllRecipeNewSiteParserTests(unittest.TestCase):

    def setUp(self):
        recipeGet = requests.get('https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/', headers=headers)
        self.recipeSoup = BeautifulSoup(recipeGet.content, 'html.parser')

        nutritionGet = requests.get('https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/fullrecipenutrition/', headers=headers)
        self.nutritionSoup = BeautifulSoup(nutritionGet.content, 'html.parser')

        with open(os.path.join(os.path.dirname(__file__),'TestData/allRecipeEachParseTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testdata = json.loads(testData)["chocolateChipCookies"]

        self.recipeParser = AllRecipeParserNewSite(self.recipeSoup, self.nutritionSoup)

    def test_parse_ingredients(self):

        for ing in self.recipeParser.ingredients:
            self.assertTrue(ing in self.testdata["ingredients"], True)

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

    ## needs to be fixed
    def test_nutrition_content(self):
        for key, amount in self.testdata["nutritionFacts"].items():
            self.assertTrue(self.recipeParser.nutritionFacts[key][0], amount)



if __name__ == '__main__':
    unittest.main()
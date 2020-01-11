import unittest

import requests
from bs4 import BeautifulSoup

from RecipeParser.src.WebRequestor import WebRequestorFactory

headers = {
    "user-agent": "ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36"
}


class PageRequestorFactoryTests(unittest.TestCase):

    def setUp(self):
        self.recipeUrl = 'https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/'
        self.recipeNutritionUrl = 'https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/fullrecipenutrition/'
        recipeGet = requests.get(self.recipeUrl, headers=headers)
        self.recipeSoup = BeautifulSoup(recipeGet.content, 'html.parser')

        nutritionGet = requests.get(self.recipeNutritionUrl, headers=headers)
        self.nutritionSoup = BeautifulSoup(nutritionGet.content, 'html.parser')


    def test_requestAllRecipePages(self):
        webFactory = WebRequestorFactory.WebRequestorFactory('https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/')
        allRecipePages = webFactory.requestSoupPage()

        self.assertTrue(allRecipePages['recipePage'].find('body')['ng-app'], self.recipeSoup.find('body')['ng-app'])

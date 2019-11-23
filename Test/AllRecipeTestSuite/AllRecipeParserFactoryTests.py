import time
import unittest
import json
import os
from threading import Thread

from bs4 import BeautifulSoup
import requests
from Parser.AllRecipeParser import AllRecipeFactory

headers = {
    "user-agent": "ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36"
}

recipes = [["https://www.allrecipes.com/recipe/10549/best-brownies/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%203",
                'https://www.allrecipes.com/recipe/10549/best-brownies/fullrecipenutrition/']
           ,["https://www.allrecipes.com/recipe/10687/mrs-siggs-snickerdoodles/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%205",
                'https://www.allrecipes.com/recipe/10687/mrs-siggs-snickerdoodles/fullrecipenutrition/']
           ,["https://www.allrecipes.com/recipe/68532/curried-coconut-chicken/?internalSource=hub%20recipe&referringId=227&referringContentType=Recipe%20Hub&clickId=cardslot%207",
                "https://www.allrecipes.com/recipe/68532/curried-coconut-chicken/fullrecipenutrition/"]
           ,["https://www.allrecipes.com/recipe/91499/general-tsaos-chicken-ii/?internalSource=recipe%20hub&referringId=227&referringContentType=Recipe%20Hub&clickId=cardslot%2022",
                "https://www.allrecipes.com/recipe/91499/general-tsaos-chicken-ii/fullrecipenutrition/"]
           ]


class AllRecipeParserFactoryTests(unittest.TestCase):
    recipes = [[
                   "https://www.allrecipes.com/recipe/10549/best-brownies/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%203",
                   'https://www.allrecipes.com/recipe/10549/best-brownies/fullrecipenutrition/']
        , [
                   "https://www.allrecipes.com/recipe/10687/mrs-siggs-snickerdoodles/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%205",
                   'https://www.allrecipes.com/recipe/10687/mrs-siggs-snickerdoodles/fullrecipenutrition/']
        , [
                   "https://www.allrecipes.com/recipe/68532/curried-coconut-chicken/?internalSource=hub%20recipe&referringId=227&referringContentType=Recipe%20Hub&clickId=cardslot%207",
                   "https://www.allrecipes.com/recipe/68532/curried-coconut-chicken/fullrecipenutrition/"]
        , [
                   "https://www.allrecipes.com/recipe/91499/general-tsaos-chicken-ii/?internalSource=recipe%20hub&referringId=227&referringContentType=Recipe%20Hub&clickId=cardslot%2022",
                   "https://www.allrecipes.com/recipe/91499/general-tsaos-chicken-ii/fullrecipenutrition/"]
               ]

    def setUp(self):
        recipeSoups = []

        for recipe in recipes:
            try:
                recipeGet = requests.get(recipe[0], headers=headers)
                if recipeGet.status_code == 404:
                    recipeSoup = None

                else:
                    recipeSoup = BeautifulSoup(recipeGet.content, 'html.parser')

                nutritionGet = requests.get(recipe[1], headers=headers)
                if nutritionGet.status_code == 404:
                    nutritionSoup = None
                else:
                    nutritionSoup = BeautifulSoup(nutritionGet.content, 'html.parser')

                recipeSoups.append([recipeSoup, nutritionSoup])
            except requests.ConnectionError as e:
                self.fail(e)
                self.stop()
            time.sleep(1)

        with open(os.path.join(os.path.dirname(__file__),'allRecipeBothTestData.json'), 'r') as testData:
            testData = testData.read()

        self.testdata = json.loads(testData)

        self.recipeParsers = []

        for recipeSoup in recipeSoups:
            recipeParser = AllRecipeFactory(recipeSoup[0], recipeSoup[1])

            self.recipeParsers.append(recipeParser.getAllRecipeParser())


    def test_parse_ingredients(self):
        counter = 0
        for recipeParser in self.recipeParsers:
            for ing in recipeParser.ingredients:
                self.assertTrue(ing in self.testdata[counter]["ingredients"], True)

            counter+=1

    def test_parse_directions(self):
        counter = 0
        for recipeParser in self.recipeParsers:
            counter1 =0
            for dire in recipeParser.directions:
                self.assertTrue(dire,  self.testdata[counter]["directions"][counter])
                counter1+=1

            counter += 1

    def test_general_recipe_info(self):
        counter = 0
        for recipeParser in self.recipeParsers:
            self.assertTrue(self.testdata[counter]["title"], recipeParser.title)
            self.assertTrue(self.testdata[counter]["cookingTime"], recipeParser.cookTime)
            self.assertTrue(self.testdata[counter]["prepTime"], recipeParser.prepTime)
            self.assertTrue(self.testdata[counter]["totalTime"], recipeParser.totalTime)

            counter += 1



    ## needs to be fixed
    def test_nutrition_content(self):
        counter = 0
        for recipeParser in self.recipeParsers:
            for key, amount in self.testdata[counter]["nutritionFacts"].items():
                test= recipeParser.nutritionFacts[key]
                self.assertTrue(recipeParser.nutritionFacts[key][0], amount)

            counter += 1

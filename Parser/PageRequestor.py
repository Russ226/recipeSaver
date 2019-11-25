from bs4 import BeautifulSoup
import requests
from Parser.AllRecipeParser import AllRecipeFactory

headers = {
    "user-agent": "ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36"
}

class PageRequestor:
    def __init__(self, url):
        self.recipeUrl = url
        #right will only work for allrecipe

        splitUrl = url.split('/')

        self.nutritionUrl = f'https://www.allrecipes.com/recipe/{splitUrl[4]}/{splitUrl[5]}/fullrecipenutrition/'


    def createSoupObj(self,url):
        r = requests.get(url, headers=headers)
        # https://www.allrecipes.com/recipe/{id}/{title}/fullrecipenutrition/
        if r.status_code == 404:
            return None
        return BeautifulSoup(r.content, 'html.parser')

    def parseAllRecipe(self):
        recipePage = self.createSoupObj(self.recipeUrl)
        nutritionPage = self.createSoupObj(self.nutritionUrl)
        recipeData = AllRecipeFactory(recipePage, nutritionPage)

        recipeData = recipeData.getAllRecipeParser()

        return recipeData
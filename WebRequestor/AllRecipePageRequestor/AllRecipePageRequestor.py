from WebRequestor import PageRequestor


class AllRecipePageRequestor(PageRequestor.PageRequestor):
    def __init__(self, url):
        super().__init__(url)


    def parseAllRecipe(self):
        allRecipePages = {}

        allRecipePages['recipePage'] = self.createSoupObj(self.recipeUrl)
        allRecipePages['nutritionPage'] = self.createSoupObj(self.nutritionUrl)

        return allRecipePages
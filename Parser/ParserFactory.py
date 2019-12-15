from Parser.AllRecipe import AllRecipeParser


class ParserFactory:
    def __init__(self, recipePage):
        self.recipePage = recipePage

    def parseRecipePage(self):
        if self.recipePage['recipeWebsiteName']is 'allRecipe':
            allRecipeParser = AllRecipeParser.AllRecipeFactory(self.recipePage['recipePage'], self.recipePage)

            return  allRecipeParser
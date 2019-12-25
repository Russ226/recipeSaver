from Parser.AllRecipe import AllRecipeParser

# pass soup obj(s) to parse depending on the website some recipes might a different nutrition
class ParserFactory:


    def parseRecipePage(self, recipePage):
        if recipePage['recipeWebsiteName']is 'allRecipe':
            allRecipeParser = AllRecipeParser.AllRecipeFactory(recipePage['recipePage'], recipePage)

            return allRecipeParser
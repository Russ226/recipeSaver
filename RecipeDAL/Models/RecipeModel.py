class Recipe:
    def __init__(self):
        pass
    def __init__(self, recipeInfo):
        self.title = recipeInfo['title']
        self.cookTime = recipeInfo['cookTime']
        self.prepTime = recipeInfo['prepTime']
        self.totalTime = recipeInfo['totalTime']
        self.ingredients = recipeInfo['ingredients']
        self.directions = recipeInfo['directions']
        self.nutritionFacts = recipeInfo['nutritionFacts']
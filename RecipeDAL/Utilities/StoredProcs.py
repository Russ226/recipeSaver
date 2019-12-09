# params
# recipetitle
# servings
# cooktime
# preptime
# totaltime
def saveRecipeProc():
    return 'call up_saveRecipe(?, ?, ?, ?, ?)'


#params
# nutritionName
# amount
# unit
# recipeId = can be null
# recipeTitle = can be null
def saveNutitionProc():
    return 'call up_saveNutrition(?, ?, ?, ?, ?)'

# params
# ingredientName
# recipeId
# recipeTitle
def saveIngredientProc():
    return 'call up_saveIngredient(?, ?, ?)'

# params
# stepNumber
# direction
# recipeId
# recipeTitle
def saveDirectionProc():
    return 'call up_saveDirection(?, ?, ?, ?)'

# params
# recipeTitle
def getRecipeByTitleProc():
    return 'call up_getRecipeByTitle(?)'

#params
# recipeId
def getNutritionForRecipeProc():
    return 'call up_getNutritionForRecipe(?)'

#params
#recipeIs
def getIngredientForRecipeProc():
    return 'up_getIngredientForRecipe(?)'

#params
#recipeId
def getDirectionsForRecipeProc():
    return 'up_getDirectionForRecipe(?)'
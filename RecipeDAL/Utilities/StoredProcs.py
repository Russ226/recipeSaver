# params
# recipetitle
# servings
# cooktime
# preptime
# totaltime
def saveRecipeProc():
    return 'call up_saveRecipe(%s, %s, %s, %s, %s)'


#params
# nutritionName
# amount
# unit
# recipeId = can be null
# recipeTitle = can be null
def saveNutitionProc():
    return 'call up_saveNutrition(%s, %s, %s, %s, %s)'

# params
# ingredientName
# recipeId
# recipeTitle
def saveIngredientProc():
    return 'call up_saveIngredient(%s, %s, %s)'

# params
# stepNumber
# direction
# recipeId
# recipeTitle
def saveDirectionProc():
    return 'call up_saveDirection(%s, %s, %s, %s)'

# params
# recipeTitle
def getRecipeByTitleProc():
    return 'call up_getRecipeByTitle(%s)'

#params
# recipeId
def getNutritionForRecipeProc():
    return 'call up_getNutritionForRecipe(%s)'

#params
#recipeIs
def getIngredientForRecipeProc():
    return 'call up_getIngredientForRecipe(%s)'

#params
#recipeId
def getDirectionsForRecipeProc():
    return 'call up_getDirectionsForRecipe(%s)'
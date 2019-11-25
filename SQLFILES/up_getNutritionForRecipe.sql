CREATE PROCEDURE `up_getNutritionForRecipe` (
	IN recipeId INT
)
BEGIN
	SELECT * FROM nutrition where recipe_id = recipeId;
END

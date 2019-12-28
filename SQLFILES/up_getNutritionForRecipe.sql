CREATE DEFINER=`root`@`localhost` PROCEDURE `up_getNutritionForRecipe`(
	IN recipeId INT
)
BEGIN
	SELECT * FROM nutrition where recipe_id = recipeId Group by nutrientName;
END
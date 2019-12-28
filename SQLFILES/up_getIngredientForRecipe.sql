CREATE DEFINER=`root`@`localhost` PROCEDURE `up_getIngredientForRecipe`(
	IN recipeId INT
)
BEGIN
	SELECT * FROM ingredients where recipe_id = recipeId Group by ingredientName ;
END
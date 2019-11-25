CREATE DEFINER=`root`@`localhost` PROCEDURE `up_getDirectionsForRecipe`(IN recipeId INT
)
BEGIN
	SELECT * FROM directions where recipe_id = recipeId;
END
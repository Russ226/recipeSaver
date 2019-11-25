CREATE PROCEDURE `up_getRecipeByTitle` (
	IN recipeTitle VARCHAR(255)
)
BEGIN

SELECT * FROM recipes where title = recipeTitle;

END

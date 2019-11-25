CREATE DEFINER=`root`@`localhost` PROCEDURE `up_saveIngredient`(
	IN ingredientName VARCHAR(255),
    IN recipeId INT,
    IN recipeTitle VARCHAR(255)
)
BEGIN
	IF recipeId IS NULL THEN
		SELECT id FROM recipes 
        where title = recipeTitle LIMIT 1 INTO recipeId;
	END IF;
    
    INSERT INTO ingredients(recipe_id, ingredientName)
    VALUES(recipeId, ingredientName);
END
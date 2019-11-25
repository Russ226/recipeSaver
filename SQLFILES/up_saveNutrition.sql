CREATE PROCEDURE `up_saveNutrition` (
	IN Nname VARCHAR(255),
    IN amount INT,
    IN unit VARCHAR(255),
    IN recipeId INT,
    IN recipeTitle varchar(255)
)
BEGIN
	IF recipeId IS NULL THEN
		SELECT id FROM recipes 
        where title = recipeTitle LIMIT 1 INTO recipeId;
	END IF;
    
    INSERT INTO nutrition(recipe_id, nutrientName, amount, unit)
    VALUES(recipeId, Nname, amount, unit);

END

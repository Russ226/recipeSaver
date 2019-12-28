CREATE DEFINER=`root`@`localhost` PROCEDURE `up_saveDirection`(
	IN stepNumber INT,
    IN direction TEXT,
    IN recipeId INT,
    IN recipeTitle varchar(255)
)
BEGIN
	IF recipeId IS NULL THEN
		SELECT id FROM recipes 
        where title = recipeTitle LIMIT 1 INTO recipeId;
	END IF;
    
    INSERT INTO directions(recipe_id, stepNumber, directionText)
    VALUES (recipeId, stepNumber, direction);
END
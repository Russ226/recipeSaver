CREATE PROCEDURE `up_createRecipe` (In recipeTitle varchar(255),
	IN servings INT,
	IN cookTime VARCHAR(255),
	IN prepTime VARCHAR(255),
	IN totalTime VARCHAR(255)
)
BEGIN
	INSERT INTO recipe(title, serving, cookTime, prepTime, totalTime)
    VALUES(recipeTitle, servings, cookTime, prepTime, totalTime);
END

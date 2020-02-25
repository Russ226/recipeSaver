call up_saveRecipe('tet', 4, '5','5','5');

call up_getRecipeByTitle('bakedChickenThighs');
select * from directions GROUP BY stepNumber ;
select * from nutrition Group by nutrientName;
Select * from nutrition where recipe_id = 20;
SELECT * FROM directions where recipe_id = 20 GROUP BY stepNumber;
select * from recipes;
select * from recipes WHERE title LIKe '%C%';
call up_searchForRecipeByTitle('C');
call up_saveNutrition('test', 1, null, null , 'Crispy and Tender Baked Chicken Thighs');

call up_getNutritionForRecipe(2);
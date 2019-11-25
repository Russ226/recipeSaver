CREATE SCHEMA IF NOT EXISTS RecipeDb; 
USE RecipeDB;

CREATE TABLE IF NOT EXISTS RecipeDb.recipes(
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(50) NOT NULL,
  servings INT,
  cookTime VARCHAR(255),
  prepTime VARCHAR(255),
  totalTime VARCHAR(255),
  created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id),
  UNIQUE KEY user(title)
);

CREATE TABLE IF NOT EXISTS RecipeDb.ingredients(
  id INT NOT NULL AUTO_INCREMENT,
  recipe_id INT NOT NULL,
  ingredientName VARCHAR(255),
  PRIMARY KEY(id),
  foreign key (recipe_id) REFERENCES recipes(id)
);

CREATE TABLE IF NOT EXISTS RecipeDb.directions(
  id INT NOT NULL AUTO_INCREMENT,
  recipe_id INT NOT NULL,
  directionText TEXT,
  stepNumber INT,
  PRIMARY KEY(id),
  foreign key (recipe_id) REFERENCES recipes(id)
);

CREATE TABLE IF NOT EXISTS RecipeDb.nutrition(
  id INT NOT NULL AUTO_INCREMENT,
  recipe_id INT NOT NULL,
  nutrientName VARCHAR(255),
  amount INT,
  unit VARCHAR(255),
  PRIMARY KEY(id),
  foreign key (recipe_id) REFERENCES recipes(id)
);
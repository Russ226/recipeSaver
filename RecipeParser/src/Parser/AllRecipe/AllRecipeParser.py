import json
import re
from logging import Logger

class AllRecipeFactory:

    def getAllRecipeParser(self, recipePage, nutritionPage):
        if(recipePage.find('body').has_attr('ng-app')):
            return AllRecipeParserNewSite(recipePage, nutritionPage)

        if(recipePage.find('body').has_attr('data-add-slash')):
            return AllRecipeParserOldSite(recipePage)

        return None



class AllRecipeParserNewSite:
    def __init__(self, recipePage, nutritionPage):
        self.ingredients = self.parseIngredients(recipePage)
        self.directions = self.parseDirections(recipePage)
        self.parseNutritionFacts(recipePage, nutritionPage)
        self.parseGeneralInfo(recipePage)


    def parseIngredients(self,recipePage):
        ingredients = []
        ingredientCol = recipePage.findAll('ul', {'class': 'dropdownwrapper'})

        for col in ingredientCol:
            rows = col.findAll('li',{'class':'checkList__line'})
            for row in rows:
              ing = row.find('label')

              if ing.has_attr('title'):
                  ingredients.append(ing['title'])
        return ingredients

    # gets total cook time ,prep time, coke time, title
    def parseGeneralInfo(self, recipePage):
        self.title = recipePage.find('h1', {'id': 'recipe-main-content'}).text # title
        timeToMake = recipePage.find('ul', {'class': 'prepTime'})

        self.cookTime = timeToMake.find('time', {'itemprop': 'prepTime'})['datetime'] if timeToMake.find('time', {'itemprop': 'prepTime'}) is not None else None
        self.prepTime = timeToMake.find('time', {'itemprop': 'cookTime'})['datetime'] if timeToMake.find('time', {'itemprop': 'cookTime'}) is not None else None
        self.totalTime = timeToMake.find('time', {'itemprop': 'totalTime'})['datetime'] if timeToMake.find('time', {'itemprop': 'totalTime'}) is not None else None

        return

    def parseDirections(self, recipePage):
        directions = []

        dirList = recipePage.findAll('ol', {'class': 'recipe-directions__list'})[0].findAll('li')

        for dire in dirList:

            dirText = dire.find('span').text.strip()

            directions.append(dirText)


        return directions


    def parseNutritionFacts(self,recipePage, nutritionPage):
        self.nutritionFacts = {}

        if nutritionPage is None:
             return

        nutRows = nutritionPage.findAll('div',{'class':'nutrition-row'})

        caloriesAndServings = nutritionPage.find('div', {'class': 'nutrition-top'}).text.replace('\n', ' ').split(':')

        self.nutritionFacts['servingsPerRecipe'] = caloriesAndServings[1].split(' ')[1]
        self.nutritionFacts['calories'] = caloriesAndServings[2]

        if nutRows is not None or len(nutRows) < 1:
            try:
                for nutRow in nutRows:
                    key = nutRow.find('span', {'class': 'nutrient-name'}).text.split(':')[0]
                    key = key[0].lower() +key[1:]
                    value = nutRow.find('span', {'aria-label': re.compile(r".*")})['aria-label']

                    if key is not None and value is not None:
                        self.nutritionFacts[key.replace(' ', '')] = value.split(' ')
            except TypeError as err:
                print(err)

        return

    def __repr__(self):
        return f'title: {self.title}\ncook time: {self.cookTime}\nprep time: {self.prepTime}\ntotal time: {self.totalTime}\nINGREDIENTS:\n{self.ingredients}\n DIRECTIONS:\n{self.directions} \nNUTRITIONS:\n{self.nutritionFacts}'



class AllRecipeParserOldSite:
    def __init__(self, recipePage):
        self.ingredients = self.parseIngredients(recipePage)
        self.directions = self.parseDirections(recipePage)
        self.parseNutritionFacts(recipePage)
        self.parseGeneralInfo(recipePage)

    def parseGeneralInfo(self, recipePage):
        self.title = recipePage.find('h1', {'class': 'heading-content'}).text  # title
        timeToMake = recipePage.find('section', {'class': 'recipe-meta-container'})

        if timeToMake is not None:
            self.cookTime = timeToMake.find('div', {'class': 'recipe-meta-item-body'}).text.strip() if timeToMake.find('div',
                            {'class': 'recipe-meta-item-body'}) is not None else None
            self.prepTime = timeToMake.find('div', {'class': 'recipe-meta-item-body'}).text.strip() if timeToMake.find('div',
                            {'class': 'recipe-meta-item-body'}) is not None else None
            self.totalTime = timeToMake.find('div', {'class': 'recipe-meta-item-body'}).text.strip() if timeToMake.find('div',
                            {'class': 'recipe-meta-item-body'}) is not None else None
        else:
            self.cookTime = None
            self.prepTime = None
            self.totalTime = None

        return

    def parseIngredients(self,  recipePage):
        ingredientList = recipePage.findAll('li', {'class': 'ingredients-item'})

        ingredients = []
        for ingredientItem in ingredientList:
            ingredient = ingredientItem.find('span', {'class':'ingredients-item-name'})

            if ingredient is not None:
                ingredient = ingredient.text.strip()
                ingredient = ingredient.replace('  ', ' ')
                ingredients.append(ingredient)

        return ingredients

    def parseDirections(self, recipePage):
        directionList = recipePage.findAll('li', {'class': 'instructions-section-item'})

        directions = []

        for direction in directionList:
            newDirection = direction.find('div', {'class': 'section-body'})

            if newDirection is not None:
                directions.append(newDirection.find('p').text)

        return directions


    def parseNutritionFacts(self, recipePage):
        self.nutritionFacts = {}

        nutRows = recipePage.findAll('div',{'class':'nutrition-row'})

        caloriesAndServings = recipePage.find('div', {'class': 'nutrition-top'}).text.replace('\n', ' ').split(':')

        self.nutritionFacts['servingsPerRecipe'] = caloriesAndServings[1].split(' ')[1]
        self.nutritionFacts['calories'] = caloriesAndServings[2]

        if nutRows is not None or len(nutRows) < 1:
            try:
                for nutRow in nutRows:
                    firstSection = nutRow.find('span', {'class': 'nutrient-name'}).text.split(':')[0].lower().split(' ')
                    secondSection = ''.join(x.capitalize() for x in firstSection[1:])
                    firstSection[0]
                    key = firstSection[0] + secondSection
                    value = re.split(r'([A-Za-z]+)' ,nutRow.find('span', {'aria-label': re.compile(r".*")})['aria-label'])

                    if key is not None and value is not None:
                        self.nutritionFacts[key] = value[:2]
            except Exception as e:
                Logger.debug(e)

        return

    def __repr__(self):
        return f'title: {self.title}\ncook time: {self.cookTime}\nprep time: {self.prepTime}\ntotal time: {self.totalTime}\nINGREDIENTS:\n{self.ingredients}\n DIRECTIONS:\n{self.directions} \nNUTRITIONS:\n{self.nutritionFacts}'

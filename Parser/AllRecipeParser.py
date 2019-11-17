import re
from logging import Logger
import datetime
class AllRecipeFactory:
    pass



class AllRecipeParserNewSite:
    def __init__(self, recipePage, nutritionPage):
        self.nutritionPage = nutritionPage
        self.recipePage = recipePage
        self.ingredients = self.parseIngredients()
        self.directions = self.parseDirections()
        self.parseNutritionFacts()
        self.parseGeneralInfo()


    def parseIngredients(self):
        ingredients = []
        ingredientCol = self.recipePage.findAll('ul', {'class': 'dropdownwrapper'})

        for col in ingredientCol:
            rows = col.findAll('li',{'class':'checkList__line'})
            for row in rows:
              ing = row.find('label')

              if ing.has_attr('title'):
                  ingredients.append(ing['title'])
        return ingredients

    # gets total cook time ,prep time, coke time, title
    def parseGeneralInfo(self):
        self.title = self.recipePage.find('h1', {'id': 'recipe-main-content'}).text # title
        timeToMake = self.recipePage.find('ul', {'class': 'prepTime'})

        self.cookTime =  timeToMake.find('time', {'itemprop': 'prepTime'})['datetime'] if timeToMake.find('time', {'itemprop': 'prepTime'}) is not None else None
        self.prepTime = timeToMake.find('time', {'itemprop': 'cookTime'})['datetime'] if timeToMake.find('time', {'itemprop': 'cookTime'}) is not None else None
        self.totalTime = timeToMake.find('time', {'itemprop': 'totalTime'})['datetime'] if timeToMake.find('time', {'itemprop': 'totalTime'}) is not None else None

        return

    def parseDirections(self):
        directions = []

        dirList = self.recipePage.findAll('ol', {'class': 'recipe-directions__list'})[0].findAll('li')

        for dire in dirList:

            dirText = dire.find('span').text.strip()

            directions.append(dirText)


        return directions


    def parseNutritionFacts(self):
        self.nutritionFacts = {}

        if self.nutritionPage is None:
             return

        nutRows = self.nutritionPage.findAll('div',{'class':'nutrition-row'})

        caloriesAndServings = self.nutritionPage.find('div', {'class': 'nutrition-top'}).text.replace('\n', ' ').split(':')

        self.nutritionFacts['servingsPerRecipe'] = caloriesAndServings[1].split(' ')[1]
        self.nutritionFacts['calories'] = caloriesAndServings[2]

        if nutRows is not None or len(nutRows) < 1:
            try:
                for nutRow in nutRows:
                    key = nutRow.find('span', {'class': 'nutrient-name'}).text.split(':')[0]
                    value = nutRow.find('span', {'aria-label': re.compile(r".*")})['aria-label']

                    if key is not None and value is not None:
                        self.nutritionFacts[key.replace(' ', '')] = value.split(' ')
            except None as e:
                Logger.debug(e)

        return

    def __repr__(self):
        return f'title: {self.title}\ncook time: {self.cookTime}\nprep time: {self.prepTime}\ntotal time: {self.totalTime}\nINGREDIENTS:\n{self.ingredients}\n DIRECTIONS:\n{self.directions} \nNUTRITIONS:\n{self.nutritionFacts}'



class AllRecipeParserOldSite:
    def __init__(self, recipePage):
        self.recipePage = recipePage
        self.ingredients = self.parseIngredients()
        self.directions = self.parseDirections()
        self.parseNutritionFacts()
        self.parseGeneralInfo()

    def parseGeneralInfo(self):
        self.title = self.recipePage.find('h1', {'class': 'heading-content'}).text  # title
        timeToMake = self.recipePage.find('section', {'class': 'recipe-meta-container'})

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

    def parseIngredients(self):
        ingredientList = self.recipePage.findAll('li', {'class': 'ingredients-item'})

        ingredients = []
        for ingredientItem in ingredientList:
            ingredient = ingredientItem.find('span', {'class':'ingredients-item-name'})

            if ingredient is not None:
                ingredient = ingredient.text.strip()
                ingredient = ingredient.replace('  ', ' ')
                ingredients.append(ingredient)

        return ingredients

    def parseDirections(self):
        directionList = self.recipePage.findAll('li', {'class': 'instructions-section-item'})

        directions = []

        for direction in directionList:
            newDirection = direction.find('div', {'class': 'section-body'})

            if newDirection is not None:
                directions.append(newDirection.find('p').text)

        return directions


    def parseNutritionFacts(self):
        self.nutritionFacts = {}

        nutRows = self.recipePage.findAll('div',{'class':'nutrition-row'})

        caloriesAndServings = self.recipePage.find('div', {'class': 'nutrition-top'}).text.replace('\n', ' ').split(':')

        self.nutritionFacts['servingsPerRecipe'] = caloriesAndServings[1].split(' ')[1]
        self.nutritionFacts['calories'] = caloriesAndServings[2]

        if nutRows is not None or len(nutRows) < 1:
            try:
                for nutRow in nutRows:
                    firstSection = nutRow.find('span', {'class': 'nutrient-name'}).text.split(':')[0].split(' ')
                    secondSection = ''.join(x.capitalize() for x in firstSection[1:])
                    key = firstSection[0]+secondSection
                    value = re.split(r'([A-Za-z]+)' ,nutRow.find('span', {'aria-label': re.compile(r".*")})['aria-label'])

                    if key is not None and value is not None:
                        self.nutritionFacts[key] = value[:2]
            except None as e:
                Logger.debug(e)

        return

    def __repr__(self):
        return f'title: {self.title}\ncook time: {self.cookTime}\nprep time: {self.prepTime}\ntotal time: {self.totalTime}\nINGREDIENTS:\n{self.ingredients}\n DIRECTIONS:\n{self.directions} \nNUTRITIONS:\n{self.nutritionFacts}'

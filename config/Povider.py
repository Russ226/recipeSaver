##instance provider for the web layer
import json
import os

import pymysql

from Parser.ParserFactory import ParserFactory
from RecipeDAL.RecipeDAL import RecipeDAL
from RecipeSaverService.RecipeSaverService import RecipeSaverService
from WebRequestor.WebRequestorFactory import WebRequestorFactory


class Provider:
    __instance = None

    @classmethod
    def createRecipeDAL(cls):
        ## read json db file


        with open(os.path.join(os.path.dirname(__file__), 'DbConfig.json'), 'r') as testData:
            config = testData.read()

        cls.config = json.loads(config)
        ## add cursosr class
        cls.config["cursorclass"] = pymysql.cursors.DictCursor

        ## return instance of the recipeDAL layer

        cls.recipeDal = RecipeDAL(**cls.config)

        return cls.recipeDal

    @classmethod
    def createWebRequestorFactory(cls):
        cls.webRequestorFactory = WebRequestorFactory()

        return cls.webRequestorFactory

    @classmethod
    def createParserFactroy(cls):
        cls.parserFactory = ParserFactory()

        return cls.parserFactory

    @classmethod
    def createRecipeSaverService(cls):
        cls.recipeSaverService = RecipeSaverService(cls.createRecipeDAL(), cls.createParserFactroy(), cls.createWebRequestorFactory())

        return cls.recipeSaverService
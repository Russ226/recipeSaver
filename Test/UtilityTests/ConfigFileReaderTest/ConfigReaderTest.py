import json
import os
import unittest

from RecipeDAL.Utilities.DbConfigReader import DbConfigReader


class ConfigReaderTest(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), 'TestData.json'), 'r') as testData:
            testData = testData.read()

        self.testData = json.loads(testData)

    def test_reader(self):
        configReader = DbConfigReader("configTest.ini")

        settings = configReader.retrieveConnectionSetting()

        self.assertTrue(settings['host'], self.testData['host'])
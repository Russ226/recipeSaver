from urllib.parse import urlparse

from WebRequestor.AllRecipePageRequestor import AllRecipePageRequestor


class WebRequestorFactory:
    def __init__(self, url):
        self.url = url
        self.netloc = urlparse(url).netloc


    def requestSoupPage(self):
        if self.netloc == 'www.allrecipes.com':
            allRecipepages = AllRecipePageRequestor.AllRecipePageRequestor(self.url)
            return allRecipepages.parseAllRecipe()
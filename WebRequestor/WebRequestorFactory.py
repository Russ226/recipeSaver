from urllib.parse import urlparse

from WebRequestor.AllRecipePageRequestor import AllRecipePageRequestor


class WebRequestorFactory:
    def __init__(self, url):
        self.url = url
        self.netloc = urlparse(url).netloc


    def requestSoupPage(self):
        if self.netloc == 'allRecipes':
            return AllRecipePageRequestor(self.url)
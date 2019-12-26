from urllib.parse import urlparse

from WebRequestor.AllRecipePageRequestor import AllRecipePageRequestor


class WebRequestorFactory:


    def requestSoupPage(self, url):
        url = url
        netloc = urlparse(url).netloc
        if netloc == 'www.allrecipes.com':
            allRecipepages = AllRecipePageRequestor.AllRecipePageRequestor(url)
            return allRecipepages.parseAllRecipe()

        else:
            raise TypeError(f"Invalid url {url}")
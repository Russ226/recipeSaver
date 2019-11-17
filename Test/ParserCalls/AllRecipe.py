entryPointsubreddit = 'https://old.reddit.com/r/the_donald/'
headers = {
    "user-agent": "ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36"
}
from bs4 import BeautifulSoup
import requests

def createSoupObj(url):
    r = requests.get(url, headers=headers)

    return BeautifulSoup(r.content, 'html.parser')

def run():
    soup = createSoupObj('https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/')
    print(soup.findAll('ul', {'class':'dropdownwrapper'})[0].findAll('li',{'class':'checkList__line'})) ## get ingredient col-#

if __name__ == "__main__":
    run()
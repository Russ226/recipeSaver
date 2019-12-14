from WebRequestor.PageRequestor import PageRequestor
# used for use cases
def main():
    page = PageRequestor('https://www.allrecipes.com/recipe/68461/buffalo-chicken-dip/?internalSource=hub%20recipe&referringId=76&referringContentType=Recipe%20Hub&clickId=cardslot%208')

    recipe = page.parseAllRecipe()

    print(recipe)

if __name__ == '__main__':
    main()
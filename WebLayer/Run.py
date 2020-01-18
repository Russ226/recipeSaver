from os import sys, path
sys.path.append('/home/russ/recipeApp/recipeSaver/')
print(sys.path)
from WebLayer.App.App import app

if __name__ == '__main__':
	app.run(threaded=True)

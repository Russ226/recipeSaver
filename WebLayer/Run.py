from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from WebLayer.App.App import app

if __name__ == '__main__':
	app.run(threaded=True)
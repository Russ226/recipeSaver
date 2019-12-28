import os
from flask import Flask



def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'dude'
	app.secret_key = os.urandom(24)
	app.register_blueprint(user, url_prefix='/user')
	app.register_blueprint(dates, url_prefix='/date')
	return app

app = create_app()

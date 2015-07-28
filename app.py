from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from model import *


@app.route('/', methods=['GET','POST'])
def hello():
	db_entries = Entry.query.all()
	entries=[]
	for e in db_entries:
		entries.append(e)
	return render_template('index.html', entries = db_entries)




@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__ =='__main__':
	app.run()
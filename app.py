
from datetime import date
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from model import *


@app.route('/')
def index():
	db_entries = Entry.query.all()
	entries=[]
	for e in db_entries:
		entries.append(e)
	return render_template('index.html', entries = entries)

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
	if request.method=='POST':
		new_entry = Entry(request.form['title'], request.form['body'], date.today())

		if new_entry.body=="" or new_entry.title=="":
			return(render_template('newpost.html', error="Title and body please!"))

		else:
			db.session.add(new_entry)
			db.session.commit()
			return redirect(url_for('index'))

	return render_template('newpost.html', error="")


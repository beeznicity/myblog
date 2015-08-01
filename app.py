
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from flask.ext.bootstrap import Bootstrap


from flask.ext.login import logout_user, login_required, login_user
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
lm = LoginManager(app)
lm.session_protection = 'strong'
lm.login_view = 'login'

from model import *
from forms import LoginForm, RegistrationForm


@app.route('/')
def index():
	db_entries = Entry.query.all()
	entries=[]
	for e in db_entries:
		entries.append(e)
	return render_template('index.html', entries = entries)


@app.route('/newpost', methods=['GET', 'POST'])
@login_required
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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid username or password.')

	return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('index'))


# @app.route('/register', methods = ['GET', 'POST'])
# def register():
# 	form = RegistrationForm()
# 	if form.validate_on_submit():
# 		user = User(email=form.email.data,
#                     username=form.username.data,
#                     password=form.password.data)
# 		db.session.add(user)
# 		db.session.commit()
# 		flash('You can now login.')
# 		return redirect(url_for('login'))

# 	return render_template('register.html', form=form)


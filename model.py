from app import db
import uuid


class Entry(db.Model):
	__tablename__ = 'entries'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	body = db.Column(db.Text)
	date= db.Column(db.Date)

	def __init__(self, title, body, date):

		self.title = title
		self.body = body
		self.date=date

	def __repr__(self):
		return '<id {}>'.format(self.id)
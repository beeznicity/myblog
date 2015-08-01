from app import db, lm
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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



"""
    Have begun implementing flask-login to handle users and linking users to posts. Don't really have a clue what i'm doing at this point.
    Definitely needs deeper dive later to grasp and complete implementation

"""

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    #posts = db.relationship("Entry", backref='author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)




    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_anonyous(self):
        return False


    def __repr__(self):
        return '<User %r>' % (self.nickname)



from sqlalchemy import false
from application import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_bcrypt import Bcrypt

db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)

class Book (db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(200))
    author_1 = db.Column(db.String(200))
    author_2 = db.Column(db.String(200))
    publisher = db.Column(db.String(200))
    category = db.Column(db.String(200))
    specific_area = db.Column(db.String(200))
    location = db.Column(db.String(200))
    copys = db.relationship("Copy", backref="book")

    def __init__ (self,title,subtitle='',author_1='',author_2='',publisher='',category='',specific_area='',location=''):
        self.title = title
        self.subtitle = subtitle
        self.author_1 = author_1
        self.author_2 = author_2
        self.publisher = publisher
        self.category = category
        self.specific_area = specific_area
        self.location = location


class Copy (db.Model):
    __tablename__ = 'copy'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    loans = db.relationship("Loan", backref="copy")
    stock= db.Column(db.String(200))
    def __init__(self,book_id):
        self.book_id = book_id
        self.stock = 'Disponível'

class User (db.Model):
    __tablename__ = 'user'
    cpf = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    email = db.Column(db.String(200))
    loans = db.relationship("Loan", backref="user")
    def __init__(self,cpf,name,phone,email):
        self.cpf = cpf
        self.name = name
        self.phone = phone
        self.email = email

class Loan (db.Model):
    __tablename__ = 'loan'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_cpf = db.Column(db.String(200), db.ForeignKey("user.cpf"))
    copy_id = db.Column(db.Integer, db.ForeignKey("copy.id"))
    date_loan = db.Column(db.DateTime)
    date_return = db.Column(db.DateTime)
    date_effective = db.Column(db.DateTime)
    obs = db.Column(db.String(500))

    def __init__ (self,user_cpf,copy_id,date_return):
        self.user_cpf = user_cpf
        self.copy_id = copy_id
        self.date_loan = datetime.now()
        self.date_return = date_return

    def return_book(self,obs):
        self.obs = obs
        self.date_effective = datetime.now()

class Login (db.Model):
    __tablename__ = 'login'
    user = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.LargeBinary(60))
    def __init__(self,user, password):
        self.user = user
        self.set_password(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def set_password(self,password):
        self.password = bcrypt.generate_password_hash(password)


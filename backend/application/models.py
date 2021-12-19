from application import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Book (db.Model):
    __tablename__ = 'book'
    id = db.Column(db.String(200), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    substitute = db.Column(db.String(200))
    author_1 = db.Column(db.String(200))
    author_2 = db.Column(db.String(200))
    author_3 = db.Column(db.String(200))
    publisher = db.Column(db.String(200))
    edition = db.Column(db.String(200))
    volume = db.Column(db.String(200))
    concentration_area = db.Column(db.String(200))
    specific_area = db.Column(db.String(200))
    location = db.Column(db.String(200))
    copys = db.relationship("Copy", backref="book")

    def __init__ (self, id,title,substitute='',author_1='',author_2='',author_3='',publisher='',edition='',volume='',concentration_area='',specific_area='',location='',):
        self.id = id
        self.title = title
        self.substitute = substitute
        self.author_1 = author_1
        self.author_2 = author_2
        self.author_3 = author_3
        self.publisher = publisher
        self.edition = edition
        self.volume = volume
        self.concentration_area = concentration_area
        self.specific_area = specific_area
        self.location = location


class Copy (db.Model):
    __tablename__ = 'copy'
    id = db.Column(db.String(200), primary_key=True)
    book_id = db.Column(db.String(200), db.ForeignKey("book.id"))
    loans = db.relationship("Loan", backref="copy")
    status = db.Column(db.String(200))
    def __init__(self,id,book_id):
        self.book_id = book_id
        self.id = id
        self.status = 'Disponível'

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
    copy_id = db.Column(db.String(200), db.ForeignKey("copy.id"))
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


from application import app
from .models import *
from .schemas import *
from flask import request,jsonify

@app.cli.command("seed")
def seed():
    db.create_all()

@app.route("/books")
def get_books():
    return jsonify (BookSchema(many = True).dump(Book.query.all()))

@app.route("/books", methods =["POST"])
def post_books():
    book = Book(**request.json)
    db.session.add(book)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/books", methods =["PUT"])
def put_books():
    edit = request.json
    book = Book.query.get(request.json['id'])
    main = BookSchema().dump(book)
    for prop in edit:
        if main[prop] != edit[prop]:
            setattr(book, prop,edit[prop])
    db.session.commit()
    return jsonify({"message":"Succesfully edited"}), 201

@app.route("/users")
def get_users():
    return jsonify(UserSchema(many= True).dump(User.query.all()))

@app.route("/users", methods =["POST"])
def post_users():
    user  = User(**request.json)
    db.session.add(user)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/users", methods=["PUT"])
def put_users():
    edit = request.json
    user = User.query.get(edit['id'])
    main = UserSchema().dump(user)
    for prop in main:
        if main[prop] != edit[prop]:
            setattr(user, prop,edit[prop])
    db.session.commit()

@app.route("/loans", methods =["POST"])
def post_loans():
    loan  = Loan(**request.json)
    db.session.add(loan)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/loans")
def get_loans():
    return jsonify(LoanSchema(many= True).dump(Loan.query.all()))

@app.route("/loans", methods =["PATCH"])
def patch_loans():
    item = request.json
    loan  = Loan.query.get(item['id'])
    loan.return_book(item['obs'])
    db.session.commit()
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/copys", methods =["POST"])
def post_copys():
    copy  = Copy(**request.json)
    db.session.add(copy)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/copys/<id>")
def get_copy(id):
    return jsonify( CopySchema().dump(Copy.query.get(id)))

@app.route("/copys", methods =["PUT"])
def patch_copys():
    item = request.json
    copy  = Copy.query.get(item['id'])
    copy.stock = item['stock']
    db.session.commit()
    return jsonify({"message":"Succesfully inserted"}), 201
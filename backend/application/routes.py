from application import app
from .models import *
from .schemas import *
from flask import request,jsonify
from flask_jwt_extended import create_access_token,set_access_cookies,jwt_required,unset_jwt_cookies,get_jwt,get_jwt_identity

from datetime import datetime,timedelta,timezone

@app.cli.command("seed")
def seed():
    db.create_all()
    login = Login('master','12345678')
    db.session.add(login)

@app.route("/books")
def get_books():
    return jsonify (BookSchema(many = True).dump(Book.query.order_by(Book.title).all()))

@app.route("/books", methods =["POST"])
@jwt_required()
def post_books():
    book = Book(**request.json)
    db.session.add(book)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/books", methods =["PUT"])
@jwt_required()
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
@jwt_required()
def get_users():
    return jsonify(UserSchema(many= True).dump(User.query.order_by(User.name).all()))

@app.route("/users", methods =["POST"])
@jwt_required()
def post_users():
    user  = User(**request.json)
    db.session.add(user)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/users", methods=["PUT"])
@jwt_required()
def put_users():
    edit = request.json
    user = User.query.get(edit['cpf'])
    main = UserSchema().dump(user)
    for prop in main:
        if main[prop] != edit[prop]:
            setattr(user, prop,edit[prop])
    db.session.commit()
    return jsonify({"message":"Succesfully edited"}), 201

@app.route("/loans", methods =["POST"])
@jwt_required()
def post_loans():
    loan  = Loan(**request.json)
    db.session.add(loan)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/loans")
@jwt_required()
def get_loans():
    return jsonify(LoanSchema(many= True).dump(Loan.query.order_by(Loan.id.desc()).all()))

@app.route("/loans", methods =["PATCH"])
@jwt_required()
def patch_loans():
    item = request.json
    loan  = Loan.query.get(item['id'])
    loan.return_book(item['obs'])
    db.session.commit()
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/copys", methods =["POST"])
@jwt_required()
def post_copys():
    copy  = Copy(**request.json)
    db.session.add(copy)
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route("/copys/<id>")
@jwt_required()
def get_copy(id):
    return jsonify( CopySchema().dump(Copy.query.get(id)))

@app.route("/copys", methods =["PUT"])
@jwt_required()
def patch_copys():
    item = request.json
    copy  = Copy.query.get(item['id'])
    copy.stock = item['stock']
    db.session.commit()
    return jsonify({"message":"Succesfully inserted"}), 201

@app.route('/login', methods=['POST'])
def login():
    user = request.json['user']
    password = request.json['password']
    if not user or not password:
        return jsonify({'message': 'invalid credentials', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = Login.query.get(user)
    if not user:
        return jsonify({'message': 'user not found', 'data': {}}), 401
    if user and user.check_password(password):
        response = jsonify({"msg": "login successful"})
        access_token = create_access_token(identity=user.user)
        set_access_cookies(response, access_token)
        return response, 201
    else:
        return jsonify({'message': 'invalid credentials', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
  response = jsonify()
  unset_jwt_cookies(response)
  return response, 200

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response
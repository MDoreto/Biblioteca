from flask_marshmallow import Marshmallow
from marshmallow import fields
from application import app
from .models import *

ma = Marshmallow(app)


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
    copys = ma.Nested("CopySchema", many=True, exclude=('book',))


class CopySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Copy
    book = ma.Nested("BookSchema", many=False, exclude=('copys',))
    status = fields.Method("getStatus")
    def getStatus(self,obj):
        if any( not loan.date_effective for loan in obj.loans):
            return "Emprestado"
        return obj.stock
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loan
    copy = ma.Nested("CopySchema", many=False)
    user = ma.Nested("UserSchema", many=False)
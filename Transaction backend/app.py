from flask import Flask, request, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource
from models import db, Transaction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class Transactions(Resource):
    def get(self):
        transactions_dict_list = [d.to_dict() for d in Transaction.query.all()]
        response = make_response(
            jsonify(transactions_dict_list),
            200,
        )
        return response

    def post(self):
        transactions = []
        for data in request.json:
            product_name = data['product_name']
            product_quantity = data['product_quantity']
            product_price = data['product_price']

            new_transaction = Transaction(
                product_name=product_name,
                product_quantity=product_quantity,
                product_price=product_price,
            )

            db.session.add(new_transaction)
            transactions.append(new_transaction)

        db.session.commit()

        transaction_dicts = [transaction.to_dict() for transaction in transactions]

        response = make_response(
            jsonify(transaction_dicts),
            201
        )

        return response

api.add_resource(Transactions, '/transactions')

# @app.route("/transactions", methods=['GET', 'POST'])
# def transaction():
#     if request.method == 'GET':
#         transactions = Transaction.query.all()
#         return make_response(jsonify([transaction.to_dict() for transaction in transactions]), 200)

#     if request.method == "POST":
#         data_list = request.get_json()
#         response_data = []

#         for data in data_list:
#             transaction = Transaction(
#                 product_name=data.get('product_name'),
#                 product_quantity=data.get('product_quantity'),
#                 product_price=data.get('product_price')
#             )
#             db.session.add(transaction)
#             db.session.commit()
            
#             response_data.append({
#                 'id': transaction.id,
#                 'product_name': transaction.product_name,
#                 'product_quantity': transaction.product_quantity,
#                 'product_price': transaction.product_price,
#             })

#     return make_response(jsonify(response_data), 201)


if __name__ == "__main__":
    app.run(debug=True)
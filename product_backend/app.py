from flask import Flask, request, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class Products(Resource):
    def get(self):
        products_dict_list = [p.to_dict() for p in Product.query.all()]
        response = make_response(
            jsonify(products_dict_list),
            200,
        )
        return response

    def post(self):
        products = []
        for data in request.json:
            name = data["name"]
            quantity = data['quantity']
            price = data['price']

            new_product = Product(
                name=name,
                quantity=quantity,
                price=price,
            )

            db.session.add(new_product)
            products.append(new_product)

        db.session.commit()

        product_dicts = [product.to_dict() for product in products]

        response = make_response(
            jsonify(product_dicts),
            201
        )

        return response

api.add_resource(Products, '/products')

class ProductById(Resource):

    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if product:
            product_dict = product.to_dict()
            response = make_response(
                jsonify(product_dict),
                200,
            )
            return response
        else:
            return make_response(jsonify({"message": "Product not found"}), 404)


    def patch(self, id):
        product = Product.query.filter_by(id=id).first()

        if not product:
            return jsonify({"message": "Product not found"}), 404

        # Check if the request content type is JSON
        if request.headers.get('Content-Type') != 'application/json':
            return jsonify({"message": "Invalid content type, JSON expected"}), 400

        data = request.get_json()

        # Ensure that data is a list (array)
        if not isinstance(data, list):
            return jsonify({"message": "Invalid JSON data format, expected a list"}), 400

        if len(data) == 0:
            return jsonify({"message": "No data provided for update"}), 400

        # Assuming you're updating a single product, so use data[0]
        update_data = data[0]

        # Update product attributes with data from the request, or keep the existing values if not provided
        product.name = update_data.get('name', product.name)
        product.quantity = update_data.get('quantity', product.quantity)
        product.price = update_data.get('price', product.price)

        db.session.commit()

        response_data = {"message": "Product updated successfully"}
        return make_response(jsonify(response_data), 200)

    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response(jsonify({"message": "Product not found"}), 404)

        db.session.delete(product)
        db.session.commit()
        return make_response(jsonify({"message": "Product deleted"}), 204)    

api.add_resource(ProductById, '/products/<int:id>')        

if __name__ == "__main__":
    app.run(debug=True)
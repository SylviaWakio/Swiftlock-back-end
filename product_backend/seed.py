from random import choice

from faker import Faker

from app import app, db
from models import Product

fake = Faker()

with app.app_context():

    Product.query.delete()

    db.session.add
    db.session.commit()
from random import choice

from faker import Faker

from app import app,db
from models import Transaction


fake = Faker()

with app.app_context():

    Transaction.query.delete()

    db.session.add_all
    db.session.commit()    
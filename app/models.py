from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

shop_cart = db.Table(
    'shop_cart',
    db.Column('user', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('product', db.Integer, db.ForeignKey('product.id'), nullable=False))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        db.session.add(self)
        db.session.commit()


    def addCart(self, product):
        self.add_to_cart.append(product)
=======
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


    def save_product(self):
        db.session.add(self)
        db.session.commit()

    def removeCart(self, product):
        self.add_to_cart.remove(product)
        db.session.commit()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric(12,2), nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)

    add_to_cart= db.relationship('User', 
        secondary = 'shop_cart',
        backref = 'add_to_cart',
        lazy = 'dynamic'
            )                      

    def __init__(self, name, price, description, image):
        self.name = name
        self.price = price
        self.description = description
        self.image = image

    def save_product(self):
        db.session.add(self)
        db.session.commit()




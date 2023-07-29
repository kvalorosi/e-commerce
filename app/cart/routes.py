from flask import render_template, Blueprint, request, redirect, url_for
from ..models import User, Product
from flask_login import current_user

cart = Blueprint('cart', __name__, template_folder='cart_templates')


@cart.route('/cart')
def show_cart():
    user = current_user
    cart_items = user.add_to_cart.all()
    return render_template('cart.html', cart_items=cart_items)


@cart.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    
    user = current_user
    product = Product.query.get(product_id)
    if product:
        user.addCart(product)
    return redirect(url_for('cart.show_cart'))


@cart.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart_items = user.add_to_cart.all()
    user = current_user
    product = Product.query.get(product_id)
    if product in cart_items:
        user.removeCart(product)


    return redirect(url_for('cart.show_cart'))




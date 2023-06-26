
from app import app

from flask import render_template
import requests

from app.models import Product

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def get_products():
    response = requests.get(f"https://fakestoreapi.com/products/")
    if response.ok:
        products = response.json()
        prod_info_list = []
        for p in products:
            product_info = {
                'ID': p['id'],
                'Name': p['title'],
                'Price': p['price'],
                'Description': p['description'],
                'Image': p['image']
            }
            prod_info_list.append(product_info)
        return render_template('products.html', data=prod_info_list)

@app.route('/products/<int:product_id>')
def get_product(product_id):
    response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    if response.ok:
        product = response.json()
        product_info = {
            'Name': product['title'],
            'Price': product['price'],
            'Description': product['description'],
            'Image': product['image']
        }
        print(product_info)
        return render_template('product.html', data=product_info)
# wsgi.py
from flask import Flask, jsonify, abort, request
import json

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Coucou' },
    { 'id': 4, 'name': 'lenumeroquatre'}
]

app = Flask(__name__)

def find_product(id):
    for product in PRODUCTS:
        if product['id'] == id:
            return product
    return None

@app.route('/')
def hello():
    return "Welcome to the World!"

@app.route('/api/v1/products')
def show_products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def show_product(id):
    product = find_product(id)
    if product == None:
        abort(404)
        return None
    else:
        product = jsonify(product)
        return product

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = find_product(id)
    if product == None:
        abort(404)
    else:
        PRODUCTS.remove(product)
        return '',204

@app.route('/api/v1/products', methods=['POST'])
def create_products():
    json = request.get_json()
    PRODUCTS.append(json)
    return '',201

@app.route('/api/v1/products/<int:id>', methods=['PATCH'])
def update_product(id):
    product = find_product(id)
    if product == None:
        abort(422)
    else:
        jsonupdate = request.get_json()
        product['name'] = jsonupdate['name']
        return '',204

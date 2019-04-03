# wsgi.py
from flask import Flask, jsonify

PRODUCTS = [
    {'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Coucou' }
]

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the World!"

@app.route('/api/v1/products')
def show_products():
    return jsonify(PRODUCTS)

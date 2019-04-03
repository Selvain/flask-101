# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class Counter:
    def __init__(self):
        self.id = 4

    def next(self):
        self.id += 1
        return self.id


class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_read_single_found(self):
        response = self.client.get("/api/v1/products/2")
        product = response.json
        result = { 'id': 2, 'name': 'Socialive.tv' }
        self.assertEqual(product, result)
        self.assertStatus(response,200)

    def test_read_single_notfound(self):
        response = self.client.get("/api/v1/products/7")
        self.assertStatus(response,404)

    def test_delete_existing_element(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertStatus(response,204)

    def test_delete_notexisiting_element(self):
        response = self.client.delete("/api/v1/products/8")
        self.assertStatus(response,404)

    def test_create_valid_element(self):
        ID = Counter()
        response = self.client.post("/api/v1/products", json={ 'id':ID.next(), 'name':'newelement'})
        self.assertStatus(response,201)

    def test_update_valid_element(self):
        response = self.client.patch("/api/v1/products/2", json={'name':'newname'})
        self.assertStatus(response,204)

    def test_update_nonvalid_element(self):
        response = self.client.patch("/api/v1/products/8", json={'name':'newname'})
        self.assertStatus(response,422)


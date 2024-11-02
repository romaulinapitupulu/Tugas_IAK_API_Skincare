from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data produk skincare
products = [
    {"id": 1, "name": "Facial Cleanser", "price": 120},
    {"id": 2, "name": "Hydrating Toner", "price": 150},
    {"id": 3, "name": "Vitamin C Serum", "price": 250},
    {"id": 4, "name": "Moisturizer", "price": 180},
    {"id": 5, "name": "Sunscreen SPF 50", "price": 200}
]

class ProductList(Resource):
    def get(self):
        return jsonify(products)

class ProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return jsonify(product)
        return {"message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": len(products) + 1,
            "name": data["name"],
            "price": data["price"]
        }
        products.append(new_product)
        return jsonify(new_product)

class UpdateProduct(Resource):
    def put(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return {"message": "Product not found"}, 404
        data = request.get_json()
        product.update(data)
        return jsonify(product)

class DeleteProduct(Resource):
    def delete(self, product_id):
        global products
        products = [p for p in products if p["id"] != product_id]
        return {"message": "Product deleted successfully"}

# Menambahkan resource ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<int:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<int:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)

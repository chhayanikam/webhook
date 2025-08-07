from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for customers
customers = {}

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer_id = str(len(customers) + 1)
    customer = {
        'id': customer_id,
        'name': data.get('name'),
        'email': data.get('email')
    }
    customers[customer_id] = customer
    return jsonify(customer), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(list(customers.values()))

@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify(customer)

@app.route('/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    customer['name'] = data.get('name', customer['name'])
    customer['email'] = data.get('email', customer['email'])
    return jsonify(customer)

@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        return jsonify({'message': 'Customer deleted'})
    return jsonify({'error': 'Customer not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

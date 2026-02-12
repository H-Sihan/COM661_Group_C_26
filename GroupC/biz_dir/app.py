# pip install flask
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

businesses = [
    {
        "id":1,
        "name":"Costa",
        "town":"London",
        "rating":4,
        "review":[]
    },
    {
        "id":2,
        "name":"Nero",
        "town":"London",
        "rating":4,
        "review":[]
    },
    {
        "id":3,
        "name":"Pret",
        "town":"London",
        "rating":4,
        "review":[]
    }
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message":"Welcome to GET Endpoint + FLASK API"})

@app.route('/api/businesses', methods=['GET'])
def get_businesses():
    return make_response(jsonify({'Businesses': businesses}))

@app.route('/api/businesses/<int:biz_id>', methods=['GET'])
def get_one_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            return make_response(jsonify(biz), 200)

    return make_response(jsonify({"Error":"Business not found"}), 404)

if __name__ == '__main__':
    app.run(debug= True)
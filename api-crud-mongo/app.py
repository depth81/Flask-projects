from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.wrappers import response

app = Flask(__name__)

#Conection to DB
app.config["MONGO_URI"] = "mongodb://localhost:27017/dbLibrary"
mongo = PyMongo(app)

#Endpoints
@app.route('/books', methods=['POST'])
def add_book():
    name = request.json['name']
    price = request.json['price']
    if name and price:
        id = mongo.db.books.insert(
            {'name':name, 'price':price}
        )
        response = jsonify({'message':'The book ' + name + ' was added successfully'})
        return response

#BSON is JSON in binary format
@app.route('/books', methods=['GET'])
def get_books():
    books = mongo.db.books.find()
    response = json_util.dumps(books) #Convert 'books' from BSON to JSON format
    return Response(response, mimetype="application/json")

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = mongo.db.books.find_one({"_id":ObjectId(id)})
    response = json_util.dumps(book)
    return Response(response,mimetype="application/json")

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    mongo.db.books.delete_one({'_id':ObjectId(id)})
    response = jsonify({"Message":"The book with id: " + id + " was deleted successfully"})
    return response

@app.route('/books/<_id>', methods=['PUT'])
def update_book(_id):
    name = request.json['name']
    price = request.json['price']
    if name and price and _id:
        mongo.db.books.update_one({"_id":ObjectId(_id["$oid"]) if '$oid' in _id else ObjectId(_id)}, 
        {"$set":{'name':name, 'price':price}})
        response = jsonify({"message":"The book " + _id + " has been updated successfuly"})
        return response


if __name__ == "__main__":
    app.run(debug=True, port=5600)
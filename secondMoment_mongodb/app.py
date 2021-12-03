from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.wrappers import response

app = Flask(__name__)

#Conection to DB
app.config["MONGO_URI"] = "mongodb://localhost:27017/dbThirdMomentMongo"
mongo = PyMongo(app)

#Endpoints
#---CUSTOMERS---
@app.route('/customers', methods=['POST'])
def add_customer():
    name = request.json['name']
    status = request.json['status']
    mobile = request.json['mobile']
    if name and status and mobile:
        id = mongo.db.customers.insert(
            {'name':name, 'status':status, 'mobile':mobile}
        )
        response = jsonify({'message':'The customer ' + name + ' was added successfully'})
        return response

#BSON is JSON in binary format
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = mongo.db.customers.find()
    response = json_util.dumps(customers) #Convert 'customers' from BSON to JSON format
    return Response(response, mimetype="application/json")

@app.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    customer = mongo.db.customers.find_one({"_id":ObjectId(id)})
    response = json_util.dumps(customer)
    return Response(response,mimetype="application/json")

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = mongo.db.customers.find_one({"_id":ObjectId(id)},{ "_id": 0, "name": 1})
    response1 = json_util.dumps(customer)
    customer_name = response1[10:-2]
    print(customer_name)
    invoices = mongo.db.invoices.find({"customer":customer_name})
    response2 = json_util.dumps(invoices)
    print(response2)
    print(len(response2))
    if response2 != '[]':
        response = jsonify({"message":"Forbidden. You have invoices to pay yet"})
        return response
    else:
        mongo.db.customers.delete_one({'_id':ObjectId(id)})
        response = jsonify({"Message":"The customer with id: " + id + " was deleted successfully"})
        return response

@app.route('/customers/<_id>', methods=['PUT'])
def update_customer(_id):
    name = request.json['name']
    status = request.json['status']
    mobile = request.json['mobile']
    if name and status and mobile and _id:
        mongo.db.customers.update_one({"_id":ObjectId(_id["$oid"]) if '$oid' in _id else ObjectId(_id)}, 
        {"$set":{'name':name, 'status':status, 'mobile':mobile}})
        response = jsonify({"message":"The customer " + _id + " has been updated successfuly"})
        return response


#---INVOICES---
@app.route('/invoices', methods=['POST'])
def add_invoice():
    date = request.json['date']
    customer = request.json['customer']
    price = request.json['price']
    balance = request.json['balance']
    if date and customer and price and balance:
        id = mongo.db.invoices.insert(
            {'date':date, 'customer':customer, 'price':price, 'balance':balance}
        )
        response = jsonify({'message':'The invoice from customer' + customer + ' was added successfully'})
        return response

#BSON is JSON in binary format
@app.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = mongo.db.invoices.find()
    response = json_util.dumps(invoices) #Convert 'invoices' from BSON to JSON format
    return Response(response, mimetype="application/json")

@app.route('/invoices/<id>', methods=['GET'])
def get_invoice(id):
    invoice = mongo.db.invoices.find_one({"_id":ObjectId(id)})
    response = json_util.dumps(invoice)
    return Response(response,mimetype="application/json")

@app.route('/invoices/<id>', methods=['DELETE'])
def delete_invoice(id):
    invoice = mongo.db.invoices.find_one({"_id":ObjectId(id)})
    response = json_util.dumps(invoice)
    index1 = int(response.find('balance'))
    balance = int(response[index1+11:-2])
    if(balance==0):
        mongo.db.invoices.delete_one({'_id':ObjectId(id)})
        response = jsonify({"Message":"The invoice with id: " + id + " was deleted successfully"})
    else:
        response = jsonify({"message":"Forbidden. The balance is not 0"})
    return response

@app.route('/invoices/<_id>', methods=['PUT'])
def update_invoice(_id):
    date = request.json['date']
    customer = request.json['customer']
    price = request.json['price']
    balance = request.json['balance']
    if date and customer and price and balance and _id:
        mongo.db.invoices.update_one({"_id":ObjectId(_id["$oid"]) if '$oid' in _id else ObjectId(_id)}, 
        {"$set":{'date':date, 'customer':customer, 'price':price, 'balance':balance}})
        response = jsonify({"message":"The invoice " + _id + " has been updated successfuly"})
        return response

#The server is listening...
if __name__ == "__main__":
    app.run(debug=True, port=5600)
    
    
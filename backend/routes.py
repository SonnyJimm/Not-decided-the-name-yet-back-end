from backend.modules import CustomerDb
import json
import datetime
from flask import request,make_response,jsonify,Response
from flask_restful import Resource,reqparse
db = CustomerDb()
customer_requerments = reqparse.RequestParser()
customer_requerments.add_argument("name",type=str,help = "Name of customer req",required=True)
customer_requerments.add_argument("age",type=str,help = "age of customer req",required=True)
customer_requerments.add_argument("reason",type=str,help = "reason of customer req",required=True)
customer_requerments.add_argument("phone_number",type=str,help = "phone of customer req",required=True)
customer_requerments.add_argument("attemptedTime",type=str,help = "attemptedTime of customer req",required=True)
class Connection(Resource):
    def get(self):
        return {"connection" : "holding"}
class QueCustomer(Resource):
    def get(self):
        customerLists = db.get()
        result=[customer.todixt() for customer in customerLists]
        return result    
    def post(self):
        args  = customer_requerments.parse_args()
        print(args)
        db.put(name=args.name,age=args.age,reason=args.reason,phone=args.phone_number,attemptedTime=args.attemptedTime)
        #db.session.add(customer)
        #db.session.commit()
        return{"args":"lol success"}
from flask import Flask,jsonify
import os
import json

booking_app=Flask(__name__)
booking_app.config['JSONIFY_PRETTYPRINT_REGULAR']=True
with (open('bookings.json')) as f:
    bookings=json.load(f)

#intro page
@booking_app.route("/",methods=['GET'])
def hello():
    return jsonify({
        "uri":"/",
        "subresource_uris":{
            "bookings":"bookings/",
            "booking":"booking/<username>"
        }
    })
@booking_app.route("/bookings/",methods=['GET'])
def get_bookings():
    return jsonify(bookings)
@booking_app.route("/booking/<username>",methods=['GET'])
def get_booking(username):
    return jsonify(bookings[username])

if __name__=='__main__':
    booking_app.run(host='0.0.0.0',port=3001,debug=True)
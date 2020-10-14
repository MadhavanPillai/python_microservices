from flask import Flask,jsonify,request
import json
from werkzeug.exceptions import NotFound,ServiceUnavailable
import requests
import os

#app and config
user_app=Flask(__name__)
user_app.config['JSONIFY_PRETTYPRINT_REGULAR']=True
user_app.env=os.environ.get("FLASK_ENV",default='development')

#host config for other services
if user_app.env=='development':
    bookings_host,movies_host,showtimes_host='http://localhost','http://localhost','http://localhost'
else:
    bookings_host=os.environ.get("BOOKINGS_HOST",default='bookings')
    movies_host=os.environ.get("MOVIES_HOST",default='movies')
    showtimes_host=os.environ.get("SHOWTIMES_HOST",default='showtimes')
#port config for other services
bookings_port='3001'
movies_port='3002'
showtimes_port='3003'
with(open('users.json')) as f:
    users=json.load(f)

@user_app.route("/",methods=['GET'])
def hello():
    return jsonify({
        "uri":"/",
        "sub_uri":{
            "all_users":"/users",
            "user":"/users/<username>",
            "user_bookings":"/users/<username>/bookings"
            #"suggested_movies":"/users/<username>/suggested"
        }
    })
@user_app.route("/users",methods=['GET'])
def user_details():
    return jsonify(users)

@user_app.route("/users/<username>",methods=['GET'])
def user(username):
    return jsonify(users[username])

@user_app.route("/users/<username>/bookings",methods=['GET'])
def suggested(username):
    if username not in users:
        raise NotFound(f"{username} not found in users database")
    try:
        user_bookings=requests.get("http://"+bookings_host+":"+bookings_port+f'/booking/{username}').json()
    except  ConnectionError:
        raise ServiceUnavailable("Booking Service is unavailable")
    #for each booking get the showtime and movie ratings
    result={}
    for date,movies in user_bookings.items():
        result[date]={}
        for movieid in movies:
            try:
                movie_details=requests.get("http://"+movies_host+":"+movies_port+f'/movie/{movieid}').json()
                result[date]=movie_details
            except ConnectionError:
                raise ServiceUnavailable("Movie service is unavailable")
    return jsonify(result)

if __name__=='__main__':
    user_app.run(host='0.0.0.0',port=3000,debug=True)
        

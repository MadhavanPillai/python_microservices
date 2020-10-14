from flask import Flask,jsonify
import json
showtimes_app=Flask(__name__)
showtimes_app.config['JSONIFY_PRETTYPRINT_REGULAR']=True

with(open('showtimes.json')) as f:
    showtimes=json.load(f)

@showtimes_app.route("/",methods=['GET'])
def hello():
    return jsonify({
        'uri':"/",
        'sub_uri':{
            "allshows":"/shows/",
            "shows@time":"/show/<timestamp>"
        }
    })

@showtimes_app.route("/shows",methods=['GET'])
def shows():
    return jsonify(showtimes)

@showtimes_app.route("/shows/<timestamp>",methods=['GET'])
def shows_at_time(timestamp):
    return jsonify(showtimes[timestamp])

if __name__=='__main__':
    showtimes_app.run(host='0.0.0.0',port=3003)
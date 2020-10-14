from flask import Flask,jsonify
import json

movie_app=Flask(__name__)
movie_app.config['JSONIFY_PRETTYPRINT_REGULAR']=True

with(open('movies.json')) as f:
    movies=json.load(f)

@movie_app.route("/",methods=['GET'])
def hello():
    return jsonify({
        'uri':'/',
        'sub_uri':{
            "movies":"/movies",
            "movie":"/movie/<movie_id>"}
    })
@movie_app.route("/movies",methods=['GET'])
def get_movies():
    return jsonify(movies)

@movie_app.route("/movie/<id>",methods=['GET'])
def get_movie(id):
    return jsonify(movies[id])

if __name__=='__main__':
    movie_app.run(host='0.0.0.0',port=3002,debug=True)
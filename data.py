from flask import Flask, jsonify, request
import csv
 
app = Flask(__name__)

with open('movies.csv', newline="") as f:
  reader = csv.reader(f)
  movies_data = list(reader)


@app.route("/")
def index():
    return jsonify({
        "data": movies_data ,
        "message": "success"
    }), 200

@app.route("/movieNames")
def names():
    director = request.args.get('Director')
    movieNames = []
    for i in movies_data:
        if i[3]==director:
            movieNames.append(i)
    return jsonify({
        "data": movieNames ,
        "message": "success"
    }), 200

@app.route("/castNames")
def castNames():
    #director = request.args.get('Director')
    movieCast = []
    for i in movies_data:
        k=i[2].split(' ')
        print(k[1])
        for n in k:
            if n=='Sam Worthington':
                movieCast.append(i)
    return jsonify({
        "data": movieCast ,
        "message": "success"
    }), 200



if __name__ == "__main__":
    app.run()

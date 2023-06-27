from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


# RETURNS THE ROOT PAGE/HOME PAGE OF OUR APPLICATION
#---------------------------------------------------
@app.route("/",methods=['GET'])

def defaultPage():
	return "Welcome to flask class", 200


if __name__ == "__main__":
	app.run(port=4000)


















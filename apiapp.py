from flask import Flask, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


#ROOT/HOME ENDPOINT 
#--------------------
@app.route('/')
def apihome():
	return jsonify({"success": "Visiting the root of the API"}), 200


# RETURNS THE MESSAGE ENDPOINT AS JSON STRING
#---------------------------------------------
@app.route("/messagestr",methods=['GET'])

def messagestr():
	message = "Default Message"
	msgstring = "Welcome to flask class"
	welcomemsg = {message : msgstring}
	myjsonstr = json.dumps(welcomemsg)

	return myjsonstr, 200


# RETURNS THE MESSAGE ENDPOINT AS JUST JSON
#-------------------------------------------
@app.route("/message",methods=['GET'])

def message():
	message = "Default Message"
	msgstring = "Welcome to flask class"
	welcomemsg = {message : msgstring}
	return jsonify(welcomemsg), 200


# RETURNS THE QUIZ ENDPOINT 
#----------------------------
@app.route("/quiz",methods=['GET'])

def quizPage():
	with open("example_2.json","r") as file:
		content = json.load(file)
	return jsonify(content), 200


# ACCEPTING URL VALUES WITH PATH PARAMETERS
# RETURNS THE QUIZ ENDPOINT WITH A PATH PARAMETER
#----------------------------------------------------
@app.route("/quizzes/<page>",methods=['GET'])

def quizPages(page):
	if page == '1':		
		with open("example_1.json","r") as file:
			content = json.load(file)
	else:
		with open("example_2.json","r") as file:
			content = json.load(file)
	return jsonify(content), 200




if __name__=="__main__":
	app.run(port=4200, debug=True)
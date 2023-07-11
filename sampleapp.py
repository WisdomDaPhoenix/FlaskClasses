from flask import Flask, request, jsonify, render_template
import json

myapp = Flask(__name__)


@myapp.route("/")  # ROUTE ROOTPAGE/HOMEPAGE

def home():
	return """
	<h1> WELCOME MESSAGE </h1> <br>
	Welcome to flask, I hope you have a nice 
	time using this framework!
	<p> My name is <strong> Mr. Wisdom </strong> </p>
	We are in class	"""




@myapp.route("/jsonpage")  # ROUTE JSON PAGE

def myjsonpage():
	d = {"Message" : "Welcome to Flask in 2023"}
	mystr = json.dumps(d)

	return mystr


@myapp.route("/niitstudents", methods=["GET"]) # ROUTE NIIT STUDENTS PAGE

def details():
	content = None

	studetails = {"data": [
	{"Name": "Derin","Age": 17,"Hobbies": ["Reading","Music"]},
	{"Name": "Elijah","Age": 28,"Hobbies": ["Drinking","Playstation"]},
	{"Name": "Daniel","Age": 27,"Hobbies": ["Singing","Coding"]},
	{"Name": "Tolu","Age": 18,"Hobbies": ["Cheating","Eating"]}
	]
	}	

	# studetails_str = json.dumps(studetails)

	if request.method == "GET":
		content = studetails

	return jsonify(content), 200


@myapp.route("/example1", methods=["GET"])  # ROUTE EXAMPLE1

def getFruit():
	with open("example_1.json","r") as file:
		content = json.load(file)

	return jsonify(content), 200



@myapp.route("/samplehtml", methods=["GET"]) # ROUTE SAMPLEHTML PAGE

def myhtmlpage():
	myvar = 40
	return render_template("mypage.html",myvar=myvar), 200



if __name__=="__main__":
	myapp.run(debug=True)









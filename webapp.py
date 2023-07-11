from flask import Flask, render_template, redirect, url_for, jsonify, request
import json


webapp = Flask(__name__)


#---------------------------------------------------------
@webapp.route("/", methods=["GET"])

def indexPage():
	return render_template("base.html"), 200


#----------------------------------------------------------


@webapp.route("/user",methods=["GET"])

def getUserPage():
	return render_template("user_dashboard.html"), 200


#----------------------------------------------------------

@webapp.route('/submitmovie',methods=['POST','GET'])

def getUserMovie():	
	d = request.args.to_dict()
	username = d['name']
	usermovie = d['movie']
	# if request.method == 'POST':
	# 	username = request.form['name']
	# 	usermovie = request.form['movie']
	# 	return render_template("user_movie_request.html",usermovie=usermovie,username=username)

	return render_template("user_movie_request.html",username=username,usermovie=usermovie), 200

 
#----------------------------------------------------------

@webapp.route('/processage',methods=['GET'])

def processUserAge():
	movie = "The Conjuring"
	age = 20
	return render_template("watchstatus.html",usermovie=movie,userage=age), 200

 
#----------------------------------------------------------

@webapp.route("/admin",methods=["GET"])

def getAdminPage():
	return redirect(url_for('getUserPage')), 301

#------------------------------------------------------

@webapp.route("/allusers",methods=["GET"])

def getUsers():
	users = {	
	"userdata": [
	{"firstname": "John",
	"lastname": "Doe",	
	"status": "user"},

	{"firstname": "Becky",
	"lastname": "Ann",
	"status": "admin"}]
	}

	with open("allusers.json","w") as file:
		json.dump(users, file, ensure_ascii=False)


	return jsonify(users), 200


@webapp.route("/search",methods=["GET"])

def searchUser():
	d = request.args.to_dict()
	username = d["name"]

	with open("allusers.json","r") as file:
		content = json.load(file)
		for item in content["userdata"]:
			if item["firstname"] == username:
				userinfo = item	

		# userinfo = [item for item in content["userdata"] if item["firstname"] == d["name"]]

	return userinfo














if __name__=="__main__":
	webapp.run(port=4800,debug=True)







# from flask import Flask, render_template, request
# from flask_cors import CORS
# import pandas as pd
# import json


# app = Flask(__name__)
# CORS(app)




# #BASE HTML PAGE
# #--------------------

# @app.route('/')

# def home():
# 	return render_template("index.html", num=45), 200





# #GET A QUOTE
# #-------------
# @app.route('/getaquote',methods=['POST','GET'])

# def quote():
# 	if request.method == 'POST':
# 		with open('requests.txt','w') as f:
# 			f.write(f"'Request': {request.form}, 'Type': {type(request.form)}")
# 		print(request.form)
# 		print(type(request.form))
# 		content = request.form['myinput']
# 		return render_template("requestquote.html", content=content), 200
# 	return render_template("requestquote.html"), 200

# if request.method == 'POST': 		
	# 	content = request.form['movie']
	# 	return render_template("user_movie_request.html"), 201

# if __name__=="__main__":
# 	app.run(port=4400, debug=True)



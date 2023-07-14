from flask import Flask, request, render_template, redirect, url_for, jsonify
import requests
import json
import pandas as pd
from getcsv import getCSVContacts


smsapp = Flask(__name__)


apiSecret = "076ad3c8b6d8e58146aef78cdbedaf49df304149"


# API Endpoint
url = "https://www.cloud.smschef.com/api/send/sms"
deviceid = "00000000-0000-0000-d7e8-e8199f60b802"


@smsapp.route("/", methods=["GET","POST"])

def tronhome():
	# Getting CSV contacts
	getCSVContacts()

	# Checking for data input
	if request.method == "POST" and request.form['send'] == "SEND NOW":
		phone_number = request.form['phone_num']
		message = request.form['msg']


		# Sending Parameters
		smsparams = {
		    "secret": apiSecret,
		    "mode": "devices",
		    "phone": phone_number,
		    "message": message,
		    "device" : deviceid,
		    "sim" : 1,
		    "priority": 1
		    }

		# Sending Message     
		response = requests.post(url, params=smsparams)
		jsonstatus = response.json()
		status = jsonstatus["message"]
		code = jsonstatus["status"]


		return render_template("tronsms.html",status=status,code=code), 201

	return render_template("tronsms.html"), 200

@smsapp.route("/contacts", methods=["GET"])

def allContacts():
	with open('contacts.json') as file:
		allinfo = json.load(file)

	return jsonify(allinfo), 200


@smsapp.route("/addcontact", methods=["GET","POST"])

def addContact():
	addmsg = "Contact added!"
	with open('contacts.json','r') as file:
		allinfo = json.load(file)

	if request.method == "POST":
		contact = request.form["contact_name"]
		number = request.form["contact_num"]
		data = {"Name": contact,"Phone number": number}
		allinfo["contacts"].append(data)


	with open('contacts.json','w') as file:
		json.dump(allinfo,file)

	getCSVContacts()

	return render_template("tronadd.html"), 200



@smsapp.route("/delcontact", methods=["GET"])

def deleteContact():
	return render_template("trondelete.html"), 200




if __name__=="__main__":
	smsapp.run(port=4000,debug=True)














# A DEFAULT SEND ACTIVITY

# your API secret from (Tools -> API Keys) page
# apiSecret = "076ad3c8b6d8e58146aef78cdbedaf49df304149"

# # API Endpoint
# url = "https://www.cloud.smschef.com/api/send/sms"


# # Sending Parameters
# smsparams = {
#     "secret": apiSecret,
#     "mode": "devices",
#     "phone": "+2348082613354",
#     "message": "Testing SMSChef",
#     "device" : "00000000-0000-0000-d7e8-e8199f60b802",
#     "sim" : 1,
#     "priority": 1
# }

# # Sending Message
# r = requests.post(url, params = smsparams)
  
# # Response from smschef in JSON
# result = r.json()



# print(result)
# Status message response in JSON
# {'status': 200, 'message': 'Message has been queued for sending!',
# 'data': False}
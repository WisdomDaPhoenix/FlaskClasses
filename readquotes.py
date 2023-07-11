import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/",methods=['GET'])

def default():
	return "Famous Quotes", 200


@app.route("/allquotes",methods=["GET"])

def allquotes():
	content = {"data": []}
	table = pd.read_csv("selectquotes.csv")
	for i in range(len(table)):
		d = {
		"Author Name": table.iloc[i]["author"],
		"Author Quote": table.iloc[i]["quote"],
		"Category": table.iloc[i]["category"]
		}
		content["data"].append(d)

	with open("allquotes.json","w") as file:
		json.dump(content, file, ensure_ascii=False)

	return jsonify(content), 200



if __name__ == "__main__":
	app.run(port=4500)







# READING THE DETAILS 

# table = pd.read_csv("Student Details.csv")

# print(table.iloc[0]) # Returns first record data only with their column headers
# print(table.iloc[0]["Students"]) # Returns first's records data from the Students column
# print(table.iloc[0]["Ages"]) # Returns first's records data from the Ages column

# print("-------------------------------------------")

# mylist = []

# for i in range(len(table)):
# 	d = {"Serial No":table.iloc[i]["Serials"],
# 	"Name":table.iloc[i]["Students"],
# 	"Age": table.iloc[i]["Ages"]}
# 	mylist.append(d)	
# print(mylist)





import pandas as pd
from flask import Flask, request, jsonify
import json
from random import choice

tableapp = Flask(__name__)

@tableapp.route("/")
def default():
	return "Generating API from samplequotes csv file"


@tableapp.route("/allsamplequotes",methods=["GET"])
def show_csv():
	table = pd.read_csv("samplequotes.csv")

	content = {"quotesdata" : []}

	for i in range(len(table)):
		d = {
		"Author": table.iloc[i]["author"],
		"Quote": table.iloc[i]["quote"],
		"Category": table.iloc[i]["category"]
		}
		content["quotesdata"].append(d)
	with open("samplequotes.json","w") as file:
		json.dump(content,file)

	return jsonify(content)


@tableapp.route("/searchquote",methods=["GET"])

def searchQuote():
	q = request.args.to_dict()
	author = q["author"]
	cat = q["category"]
	with open("samplequotes.json","r") as file:
		content = json.load(file)
		quoteslist = [item["Quote"] for item in content["quotesdata"] if item["Author"] == author and item["Category"] == cat]
		randomquote = choice(quoteslist)


	return jsonify({"Random Quote": randomquote})













if __name__=="__main__":
	tableapp.run(port=5400,debug=True)









# print("---------------------------------------------------------------------")



# input()

# # print(table.iloc[0])
# print('---------------------------------------------------------------------')
# print(table.iloc[0]["category"])
# print(table.iloc[0]["quote"])
# print(table.iloc[0]["author"])





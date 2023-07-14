import pandas as pd

def getCSVContacts():
	myjson = pd.read_json('contacts.json')
	names = [myjson.iloc[i]["contacts"]["Name"] for i in range(len(myjson))]
	numbers = [myjson.iloc[i]["contacts"]["Phone number"] for i in range(len(myjson))]


	data = pd.DataFrame({
		"Contact Names": names,
		"Phone Numbers": numbers
		})
	
	data.to_csv('static/contacts.csv')



import json
mycontacts = {"contacts": [{
	"Name": "Wisdom Enefiok",
	"Phone number": "08082613354"
}]}

with open("contacts.json","w") as file:
	json.dump(mycontacts,file)




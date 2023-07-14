from string import printable
from random import choices
import json
import os

print("""Enter what operation you would love to perform below \n 1. Generate a Password for site \n 2. Login to site""")

option = int(input("Choose 1 or 2 from above: "))

allkeys = []
if option == 2:
    with open("vault.json","r") as file:
        siteinfo = json.load(file)
        keyslist = [list(item) for item in siteinfo["Passwords"]]

    print("Keys list: ", keyslist)
    for i in range(len(keyslist)):
        allkeys = allkeys + keyslist[i]
    
    loginsite = input("Enter name of website: ")
    if loginsite not in allkeys:
        print("Login site not in your vault or list of sites")
    else:
        for item in siteinfo["Passwords"]:
            if loginsite in item:
                print(f"Your password for {loginsite} is {item[loginsite]}")

elif option == 1:   


    allstr = printable[ :-2]

    if os.path.exists("vault.json") != True:
        

        # GENERATING JSON
        sitepasswords = {"Passwords": []}

        # COLLECTING SITE INFO
        website = input("Enter name of website: ")
        passlist = choices(allstr,k=8)
        newpassword = ''.join(passlist)
        print(f"Your Generated password for {website} is {newpassword}")

        sitepasswords["Passwords"].append({website: newpassword})
        with open("vault.json","w") as file:
            json.dump(sitepasswords,file)

        print("Password added to vault!")

    else:
        # COLLECTING OLD PASSWORDS INFO
        with open("vault.json","r") as file:
            oldinfo = json.load(file)

        # COLLECTING SITE INFO
        website = input("Enter name of website: ")
        passlist = choices(allstr,k=8)
        newpassword = ''.join(passlist)
        print(f"Your Generated password for {website} is {newpassword}")

        oldinfo["Passwords"].append({website: newpassword})
        newinfo = oldinfo
        
        with open("vault.json","w") as file:
            json.dump(newinfo,file)
        print("Your password vault has been updated!")
else:
    print("Invalid option entered! ")




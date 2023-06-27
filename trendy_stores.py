import json
from bson import json_util

class Trendystores():
    def __init__(self):
        msg = "Empty Inventory"
        self.old = {}
        self.pricelist = {"data": [self.old,{"Message": msg}]}
        with open('Inventory.json','w') as file:
            file.write(json_util.dumps(self.pricelist))
        print("Trendy Stores Inventory file! No inventory Items ")


    def displayItems(self):
        with open('Inventory.json','r') as file:
            content = json.load(file)
        return f"Items and Prices are listed: \n {content}"

    def emptyFile(self):
        with open('Inventory.json','r') as file:
            content = json.load(file)
        x = content["data"][0]
        self.old.update(x)
        print("Old updated: ",self.old)
        open('Inventory.json','w').close()   # Empties file of its contents

    def updateItems(self, newitem, price):
        self.emptyFile()
        self.old.update({newitem:price})
        msg = "Inventory contains items"
        with open('Inventory.json','w') as file:
            d = {"data": [self.old,{"Message": msg}]}
            file.write(json_util.dumps(d))
        print(self.displayItems())
        print(f"File Updated successfully!")


    def deleteItem(self,item):
        with open('Inventory.json', 'r+') as file:
            content = json.load(file) # Load contents
            print(f"File's default content: {content}")
            print('-----------------------------------------------------')
            del content["data"][0][item]
            print('-----------------------------------------------------')
            print(f"File's new content: {content}")
            file.write(json_util.dumps(content))
        print(self.displayItems())

# TEST INPUTS: 

# 'Gucci bag', 16000
# 'Rolex', 250000
# 'Denim shirt',84000
# 'Chelsea boots',42000
# 'Shoe tree',3500
# 'Diamond lace',29000

# -------------- INSTANTIATING THE CLASS WITH ' t ' ------------------------------
t = Trendystores()
print(t.displayItems())
t.updateItems('Gucci bag', 16000)
t.updateItems('Rolex', 250000)
t.updateItems('Denim shirt',84000)
t.updateItems('Chelsea boots',42000)

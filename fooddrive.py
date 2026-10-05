import os.path

if not os.path.exists('inventory.txt'):
    message = open('inventory.txt','w')
    message.close()
else:
    message_inventory = open('inventory.txt','r')
    content = message_inventory.read()
    print(content)
    message_inventory.close()

class Inventory:
    def__init__()
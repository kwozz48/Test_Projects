
#Program simulates a 'fantasy game' with dictionaries

import pprint

def displayInventory (inventory): #Neatly displays inventory

    total = 0

    for a, b in inventory.items():
        print (str(b) + ' ' + a + '\n')
        total += b #Prints total number of items in inventory
    print ('Total number of items: ' + str(total) + '\n\n\n')

def addToInventory (inventory, addedItems): #Adds items from the 'dragonLoot' list to the 'inventory' dictionary

    total = 0

    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        elif i not in inventory:
            inventory [i] = 1

    for a,b in inventory.items():
        print (str(b) + ' ' + a + '\n')
        total += b #Prints total number of items in inventory
    print ('Total number of items: ', total)

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(inventory)
addToInventory(inventory, dragonLoot)
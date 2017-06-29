def displayInventory(inventory):
    print('Inventory:')
    inventorySum = 0
    for key in inventory.keys():
        itemCount = inventory[key]
        print(str(itemCount) + ' ' + key)
        inventorySum += itemCount
    print('Total number of items: ' + str(inventorySum))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)    

def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    addToInventory(stuff, dragonLoot)
    displayInventory(stuff)

main()

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    count = 0
    print("Inventory:")
    for key in inventory:
        print(inventory[key], key)
        count = count + inventory[key]
    print("Total number of items:", count)
##displayInventory(stuff)
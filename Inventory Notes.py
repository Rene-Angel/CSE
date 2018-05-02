import string


class Item(object):
    def __init__(self, name, attack, armor, weight, price):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price


class Inventory(object):
    def __init__(self):
        self.items = {}  # Creates the List to place in 'items'

    def take(self, item):  # By creating the take method, it can add in an item to the inventory
        self.items[item.name] = item
    #
    # def drop(self, item):
    #     inventory.remove[item]

    def print_inventory(self):  # Adds or 'joins' in other callable categories for balance?
        # print('\t'.join(['Name', 'Atk', 'Arm', 'Lb', 'Val'])) # This would add in other values to be printed
        for item in self.items.values():  # With the current changes, it only prints the name :)
            print('\t'.join([str(x) for x in [item.name]]))  # , item.attack, item.armor, item.weight, item.price]]))
        # for item in self.items():  # Lines of Code aren't callable and creates a TypeError
            # print(item.name)


Sword = Item('Sword', 12, 0, 10, 20)  # By creating the object outside of the inventory, it can be added
inventory = Inventory()
inventory.take(Sword)  # Adding this would call an item and add it into the inventory list
# inventory.take(Item('Sword', 15, 0, 12, 20))  # Adding this would create the object within the inventory
inventory.print_inventory()

# while True:

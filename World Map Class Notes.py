class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, atk_dmg, weight):
        super(Weapon, self).__init__(name, weight)
        self.atk_dmg = atk_dmg


class Sword(Weapon):
    def __init__(self, ):
        super(Sword, self).__init__('sword', 15, 5)


# class Consumable(Item):
#     def __init__(self, name, effect):
#         super(Consumable, self).__init__(name, weight)
#         self.effect = effect


class Character(object):
    def __init__(self, name, hp, atk, stats, inv):
        self.name = name
        self.hp = hp
        self.stats = stats
        self.inv = inv
        self.atk = atk

    # def atk(self, target):
    #     if target.damage(self.atk):
    #         print("You took Damage.")
    #
    # def self_dmg(self, dmg):
    #     self.hp -= dmg


class Inventory(object):
    def __init__(self):
        self.items = {}

    def take(self, item):
        self.items[item.name] = item
    #
    # def drop(self, item):
    #     self.items.remove[item]

    def print_inventory(self):
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name]]))


class Room(object):
    def __init__(self, name, north, south, east, west, inv, character, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.inv = Inventory()
        self.character = character

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


entrance = Room("Hideout Entrance", None, 'sewer_tunnel', None, None, {Sword}, None,
                "The only way of entering the secret hideout (To be honest, its just a manhole in the middle of a "
                "street). A sword was weirdly laying on the floor, someone must have dropped it. To the north is a "
                "tunnel with a faint light.")
sewer_tunnel = Room('Sewers', 'entrance', None, None, None, {None}, None,
                    "There was an abandoned lantern on the floor, but by the looks of it you were not alone.")

inventory = Inventory()
current_node = entrance
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()

    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
            print("")

    if command == 't':
        print('Take What?')
        input('>_').lower()
        if input == current_node.inv:
            try:
                inventory.take(current_node.inv)
            except KeyError:
                print("There's nothing to take.")

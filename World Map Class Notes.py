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
        self.empty = True

    def take(self, item):
        self.items[item.name] = item
        self.empty = False

    #
    # def drop(self, item):
    #     self.items.remove[item]

    def print_inventory(self):
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name]]))


class Room(object):
    def __init__(self, name, north, south, east, west, item, character, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = item
        self.character = character

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

sword = Sword()

START = Room("Main Hall - Entrance", None, 'HALL', 'LIBRARY', 'LABORATORY', [Sword], None,
             "You are at the entrance of this dark dungeon. A large dark oak wood door stands at your northern side "
             "locked. To your east is a candle lit corridor leading to a circular room. As for your west, a similar "
             "corridor although there were not any candles, leading to an triangular room.")
LIBRARY = Room("Library", None, None, None, 'START', [Sword], None,
               "This room has walls filled with books, and tables in order with chairs surrounding them. A locked book "
               "case grabs your attention however, with a key inside.")
LABORATORY = Room("Alchemy Laboratory", None, None, 'Start', None, [None], None,
                  "shelves on the walls are stacked with various ingredients and potions. The floor is marked with an "
                  "alchemist's circle of transmutation, and there is a table with a glowing sword and potion.")
HALL = Room("Main Hall - Hallway", 'START', 'DINING', None, None, [None], None,
            "The Main Hall of this dungeon continues toward south. Skeletal corpses lay on the floor scorched. There "
            "was a faintly lit lantern on the floor, but by the looks of it you were not alone. You hear footsteps.")
DINING = Room("Dining Room", 'HALL', 'QUARTERS', 'KITCHEN', None, [None], None,
              "A large round table stands before you with a daggers stabbed through it as if a group of rogues were "
              "plotting here for a quest. The dorms are to your south, where you still hear footsteps.")

controls = "t = take" \
           "i = inventory" \
           "n, s, e, w = moving to rooms"
inventory = Inventory()
current_node = START
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

    if command == 'i':
        print(inventory.print_inventory())
    elif inventory:
        print("You have nothing in your inventory.")

    if command == 't':
        print('Take What?')
        input('>_').lower()
        if input == current_node.item:
            try:

            except KeyError:
                print("There's nothing to take.")

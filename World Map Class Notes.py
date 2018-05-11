class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, attack, price):
        super(Weapon, self).__init__(name, price)
        self.attack = attack


class Consumable(Item):
    def __init__(self, name, effect, price):
        super(Consumable, self).__init__(name, price)
        self.effect = effect


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword", 5, 10)


class Troll_axe(Weapon):
    def __init__(self):
        super(Troll_axe, self).__init__("Troll Axe", 25, 15)


class War_axe(Weapon):
    def __init__(self):
        super(War_axe, self).__init__("War Axe", 15, 20)


class Health_potion(Consumable):
    def __init__(self):
        super(Health_potion, self).__init__("Health Potion", 100, 100)


class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__("Apple", 5, 1)


class Branch(Weapon):
    def __init__(self):
        super(Branch, self).__init__("Tree Branch", 10, 1)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Dagger", 15, 10)


class Ragnarok(Weapon):
    def __init__(self):
        super(Ragnarok, self).__init__("Ragnarok", 25, 50)


class Egg(Consumable):
    def __init__(self):
        super(Egg, self).__init__("Egg", 10, 5)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__("Stick", 1, 1)


class Character(object):
    def __init__(self, name, health, attack, stats, inv):
        self.name = name
        self.health = health
        self.stats = stats
        self.inv = inv
        self.attack_amt = attack

    def attack(self, target):
        if target.damage(self.attack_amt):
            print("You took Damage.")

    def take_damage(self, dmg):
        self.health(dmg)


class Room(object):
    def __init__(self, name, north, south, east, west, room_items, character, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.items = room_items
        self.character = character

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


sword = Sword()
dagger = Dagger()
egg = Egg()
apple = Apple()
trollaxe = Troll_axe()
waraxe = War_axe()
stick = Stick()
healthpotion = Health_potion()
ragnarok = Ragnarok()
branch = Branch()

player = Character(None, 500, 25, None, [ragnarok])
troll = Character("Troll", 150, 25, None, [trollaxe])
goblin = Character("Goblin", 100, 10, None, [dagger])
skeleton = Character("Skeleton", 75, 15, None, [sword])
dragon = Character("Dragon", 1000, 45, None, [None])
ghost = Character("Ghost", 50, 10, None, [None])

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
inventory = {}
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
    elif command == 'inventory':
        if len(player.inv) > 0:
            print("You have the following items in your inventory: ")
            for item in player.inv:
                print(item.name)
        else:
            print("You have nothing in your inventory.")
    elif command == 'take':
        item_requested = command[5:]
        found = False
        for item in current_node.items:
            if item.name == item_requested:
                player.inv.append(item)
                for items in player.inv:
                    print("You take %s." % item_requested)
                    print("You have %s in your inventory." % item.name)
                    print()
                found = True
                current_node.items.remove(item)
            else:
                print("There's nothing there to take.")

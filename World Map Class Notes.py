class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name)
        self.attack = attack


class Consumable(Item):
    def __init__(self, name, effect):
        super(Consumable, self).__init__(name)
        self.effect = effect


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword", 5)


class Troll_axe(Weapon):
    def __init__(self):
        super(Troll_axe, self).__init__("Troll Axe", 25)


class War_axe(Weapon):
    def __init__(self):
        super(War_axe, self).__init__("War Axe", 15)


class Health_potion(Consumable):
    def __init__(self):
        super(Health_potion, self).__init__("Health Potion", 100)


class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__("Apple", 5)


class Branch(Weapon):
    def __init__(self):
        super(Branch, self).__init__("Tree Branch", 10)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Dagger", 15)


class Ragnarok(Weapon):
    def __init__(self):
        super(Ragnarok, self).__init__("Ragnarok", 25)


class Egg(Consumable):
    def __init__(self):
        super(Egg, self).__init__("Egg", 10)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__("Stick", 1)


class Character(object):
    def __init__(self, name, health, attack, stats, weapon, inv):
        self.weapon = weapon
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

    def equip(self, item):
        if isinstance(item, Weapon):
            print("---------------------------------------------------------------------------------------------")
            print("New item equipped.")


class Room(object):
    def __init__(self, name, north, south, east, west, roominv, character, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.roominv = roominv
        self.character = character

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

        # def addtoinventory(self, item):


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

player = Character(None, 500, 25, None, [ragnarok], [apple])
troll = Character("Troll", 150, 25, None, [trollaxe], [egg])
goblin = Character("Goblin", 100, 10, None, [dagger], [egg])
skeleton = Character("Skeleton", 75, 15, None, [sword], [None])
dragon = Character("Dragon", 1000, 45, None, [None], [None])
ghost = Character("Ghost", 50, 10, None, [None], [None])

START = Room("Main Hall - Entrance", None, 'HALL', 'LIBRARY', 'LABORATORY', [sword], troll,
             "You are at the entrance of this dark dungeon. A large dark oak wood door stands at your northern side "
             "locked. To your east is a candle lit corridor leading to a circular room. As for your west, a similar "
             "corridor although there were not any candles, leading to an triangular room.")
LIBRARY = Room("Library", None, None, None, 'START', [sword], None,
               "This room has walls filled with books, and tables with chairs surrounding them. A locked book "
               "case grabs your attention however, with a key inside.")
LABORATORY = Room("Alchemy Laboratory", None, None, 'Start', None, [None], None,
                  "There are shelves on the walls stacked with various ingredients and potions. The floor is marked "
                  "with an alchemist's circle of transmutation, and there is a small table in the corner of the room.")
HALL = Room("Main Hall - Hallway", 'START', 'DINING', None, None, [None], None,
            "The Main Hall of this dungeon continues toward south. Skeletal corpses lay on the floor that have been "
            "recently scorched. There was a faintly lit lantern on the floor, but by the looks of it you are not "
            "alone. You hear footsteps.")
DINING = Room("Dining Room", 'HALL', 'QUARTERS', 'KITCHEN', None, [None], None,
              "A large round table stands before you with a daggers stabbed through it as if a group of rogues were "
              "plotting here for a kill contract. The dorms are to your south, where you still hear footsteps.")

inventory = []
current_node = START
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
short_look = ['l']
# interactions = ['take', 'inventory', 'use']
# short_interactions = ['t', 'i', 'u']
print(" __          __  _                          _ \n"
      " \ \        / / | |                        | |\n"
      "  \ \  /\  / /__| | ___ ___  _ __ ___   ___| |\n"
      "   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |\n"
      "    \  /\  /  __/ | (_| (_) | | | | | |  __/_|\n"
      "     \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)\n"
      "---------------------------------------------------------------------------------------------\n"
      "Welcome to the game realm, player. You will have to make every move in this game count. For if you don't, you "
      "lose(literally). Have fun in this game, and if you need to look at the controls type in 'help'.\n"
      "---------------------------------------------------------------------------------------------\n"
      "Your journey begins in...")
print(current_node.name)
print(current_node.description)
print("---------------------------------------------------------------------------------------------")
while True:
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    elif command in directions:
        try:
            current_node.move(command)
            print("---------------------------------------------------------------------------------------------")
            print(current_node.name)
            print(current_node.description)
            print("---------------------------------------------------------------------------------------------")
        except KeyError:
            print("You cannot go this way.")
            print("")

    if command == 'help':
        print("---------------------------------------------------------------------------------------------")
        print("t = take")
        print("i = inventory")
        print("u = use")
        print("n, s, e, w = moving in directions 'North', 'South', 'East', 'West'")
        print("---------------------------------------------------------------------------------------------")

    if command == 'w':
        print("---------------------------------------------------------------------------------------------")
        if len(player.weapon) > 0:
            print("You have the following weapons equipped:")
            for item in player.weapon:
                print(item.name)
            print("---------------------------------------------------------------------------------------------")
        elif len(player.weapon) < 0:
            print("You have no weapons equipped.")
            print("---------------------------------------------------------------------------------------------")

    if command == 'i':
        print("---------------------------------------------------------------------------------------------")
        if len(player.inv) > 0:
            print("You have the following items in your inventory: ")
            for item in player.inv:
                print(item.name)
            print("---------------------------------------------------------------------------------------------")
        elif len(player.inv) < 0:
            print("You have nothing in your inventory.")
            print("---------------------------------------------------------------------------------------------")

    if command == 't':
        print("---------------------------------------------------------------------------------------------")
        print("What do you want to take?")
        print("---------------------------------------------------------------------------------------------")
        item_requested = input(">_ ")
        found = False
        for item in current_node.roominv:
            if item.name == item_requested:
                player.inv.append(current_node.roominv)
                print("---------------------------------------------------------------------------------------------")
                print("You take %s." % item_requested)
                print("You now have %s in your inventory." % item.name)
                print("---------------------------------------------------------------------------------------------")
                if item in player.inv:
                    found = True
                    current_node.roominv.remove(item)
            else:
                print("---------------------------------------------------------------------------------------------")
                print("There's no item that goes by %s." % item_requested)
                print("---------------------------------------------------------------------------------------------")
    # elif command == 'take':
    #     item_requested = command[5:]
    #     found = False
    #     for item in current_node.roominv:
    #         if item.name == item_requested:
    #             player.inv.append(item)
    #             if item in player.inv:
    #                 print("You take %s." % item_requested)
    #                 print("You have %s in your inventory." % item.name)
    #                 print("")
    #             found = True
    #             current_node.roominv.remove(item)
    #         else:
    #             print("There's nothing there to take.")

    if command in short_look:
        print("---------------------------------------------------------------------------------------------")
        if len(current_node.roominv) > 0:
            print("Item(s) in your area:")
            for Item in current_node.roominv:
                print(Item.name)
            print("---------------------------------------------------------------------------------------------")
        elif len(current_node.roominv) < 0:
            print("There are no Items in your area.")
            print("---------------------------------------------------------------------------------------------")

    if command == '':
        print("---------------------------------------------------------------------------------------------\n"
              "You die by the fear of shock from not doing anything.\n"
              "---------------------------------------------------------------------------------------------\n"
              "   _____                         ____                 _ \n"
              "  / ____|                       / __ \               | |\n"
              " | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |\n"
              " | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |\n"
              " | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|\n"
              "  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)\n"
              "---------------------------------------------------------------------------------------------")
        quit(0)

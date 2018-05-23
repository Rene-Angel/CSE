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
    def __init__(self, name, health, attack, weapon, inv):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.inv = inv
        self.attack_amt = attack

    def take_damage(self, dmg):
        self.health -= dmg


class Enemy(Character):
    def __init__(self, name, health, attack, weapon, inv):
        super(Enemy, self).__init__(name, health, attack, weapon, inv)


class Room(object):
    def __init__(self, name, north, south, east, west, roominv, enemy, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.roominv = roominv
        self.enemy = enemy

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

player = Character(None, 500, 25, [ragnarok], [apple])
troll = Enemy("Troll", 150, 25, [trollaxe], [egg])
goblin = Enemy("Goblin", 100, 10, [dagger], [egg])
skeleton = Enemy("Skeleton", 75, 15, [sword], [None])
dragon = Enemy("Dragon", 1000, 45, [None], [None])
ghost = Enemy("Ghost", 50, 10, [None], [None])
prisoner_spirit = Enemy("Prisoner's Spirit", 125, 30, [None], [None])
mimic = Enemy("Mimic", 300, 25, [None], [None])

START = Room("Main Hall - Entrance", None, 'HALL', 'LIBRARY', 'LABORATORY', [sword, apple], troll,
             "You are at the entrance of this dark dungeon. A large dark oak wood door stands at your northern side "
             "locked. To your east is a candle lit corridor leading to a circular room. As for your west, a similar "
             "corridor although there were not any candles, leading to an triangular room.")
LIBRARY = Room("Library", None, None, None, 'START', [sword], None,
               "This room has walls filled with books, and tables with chairs surrounding them. A locked book "
               "case grabs your attention however, with a key inside.")
LABORATORY = Room("Alchemy Laboratory", None, None, 'Start', None, [None], None,
                  "There are shelves on the walls stacked with various ingredients and potions. The floor is marked "
                  "with an alchemist's circle of transmutation, and there is a small table in the corner of the room.")
HALL = Room("Main Hall - Hallway", 'START', 'DINING', 'CORRIDOR', None, [None], None,
            "The Main Hall of this dungeon continues toward a dining area to the south, and another hall to the east. "
            "Skeletal corpses lay on the floor that have been recently scorched. There was a faintly lit lantern on "
            "the floor, but by the looks of it you are not alone. You hear footsteps.")
CORRIDOR = Room("Main Hall - Corridor", 'CLOSET', 'KITCHEN', 'DEAD_END', 'HALL', [None], None,
                "A dead end is is lead to your east, the main hallway to the west, the kitchen to your south, "
                "and a closet to your north. There are more corpses on the floor in a trail leading you to the dead "
                "end. You hear footsteps once more...")
KITCHEN = Room("The Kitchen", 'CORRIDOR', None, 'LOCKER', 'DINING', [None], None,
               "The corridor is to the north, dining room to west, and frozen meat locker to the east. A sink filled "
               "with unwashed pots and pans releases an odor most foul. Many food items though seem fresh but rotten, "
               "although there is a striking red fruit that stands out the most. Luckily you know not to eat anything "
               "that's fake or poisoned.")
LOCKER = Room("Meat Locker", None, None, None, 'KITCHEN', [None], None,
              "You enter the frozen meat locker from the disgusting kitchen. The meat of many animals haunts your "
              "mind as you see them mutilated and hanged on hooks, but there are also more bodies and even they are "
              "hanged here.\nWhy would anybody do this?")
DINING = Room("Dining Room", 'HALL', 'QUARTERS', 'KITCHEN', None, [None], None,
              "A large round table stands before you with a daggers stabbed through it as if a group of rogues were "
              "plotting here for a kill contract. The dorms are to your south, where you still hear footsteps.")
QUARTERS = Room("The Quarters", 'DINING', None, 'WEAPONS', 'JAIL', [None], None,
                "You enter inside what seems like a quarter room for mercenaries. They lay before you in their beds, "
                "but they were slain in their sleep. Their spirits still haunt the room though. The dining room is to "
                "the north, the weapons room to your west, and the jail room to the east.")
JAIL = Room("Jail room", None, None, None, 'QUARTERS', [None], None,
            "You enter the jail room finding more corpses laying on the floor in each cell. Their lives were taken by "
            "an unnatural presence, and their spirits haunt the walls and objects crying, 'FREE ME!'. The room leads "
            "back to the quarters to the west.")
WEAPONS = Room("Weapons Room", None, None, 'QUARTERS', None, [None], None,
               "All the weapons before you have been demolished to pieces. Although each and every chest around has "
               "been looted. There were still some chests that have been untouched. The room leads back to the "
               "quarters to the east.")

inventory = []
current_node = START
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
# interactions = ['take', 'inventory', 'use']
# short_interactions = ['t', 'i', 'u']

print("---------------------------------------------------------------------------------------------\n"
      " __          __  _                          _ \n"
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
        print("---------------------------------------------------------------------------------------------\n"
              "You quit the game. Goodbye!\n"
              "---------------------------------------------------------------------------------------------\n"
              "   _____                         ____                 _ \n"
              "  / ____|                       / __ \               | |\n"
              " | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |\n"
              " | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |\n"
              " | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|\n"
              "  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)\n"
              "---------------------------------------------------------------------------------------------")
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
    elif command in directions:
        try:
            current_node.move(command)
            print("---------------------------------------------------------------------------------------------")
            print(current_node.name)
            print(current_node.description)
            if len(current_node.enemy) < 0:
                print("There are no enemies nearby.")
            elif len(current_node.enemy) > 0:
                print("Hostiles nearby:")
                for Enemy in current_node.enemy:
                    print(Enemy.name)
            print("---------------------------------------------------------------------------------------------")
        except KeyError:
            print("---------------------------------------------------------------------------------------------")
            print("You cannot go that way.")
            print("---------------------------------------------------------------------------------------------")

    if command == 'a':
        print("---------------------------------------------------------------------------------------------\n")
        print("%s had appeared!\n" % current_node.enemy.name)
        print("---------------------------------------------------------------------------------------------\n"
              "Would you like to attack? (yes/no)\n"
              "---------------------------------------------------------------------------------------------\n")
        answer = input()
        if answer == 'yes':
            current_node.enemy.health -= player.attack_amt
            print("You attacked %s." % current_node.enemy.name)
            print("They took %s damage." % player.attack_amt)
            print("---------------------------------------------------------------------------------------------\n")
        elif answer == 'no':
            player.health -= current_node.enemy.attack_amt
            print("You failed to attack, so they took advantage.")
            print("You stumble... and took %s damage." % current_node.enemy.attack_amt)
            print("---------------------------------------------------------------------------------------------\n")
        else:
            print("What are you doing? You are in a battle!"
                  "---------------------------------------------------------------------------------------------\n")
            player.health -= current_node.enemy.attack_amt
            print("You failed to attack, so they took advantage.")
            print("You stumble... and took %s damage." % current_node.enemy.attack_amt)
            print("---------------------------------------------------------------------------------------------\n")
        if current_node.enemy.health < 0:
            print("The enemy has fallen, and you continue with your journey.")
        elif player.health < 0:
            print("YOU HAVE FALLEN AND YOU CAN'T GET UP! CALL 1-800-LIFE-ALERT")
            print("The ambulance didn't make it in time."
                  "---------------------------------------------------------------------------------------------\n"
                  "   _____                         ____                 _ \n"
                  "  / ____|                       / __ \               | |\n"
                  " | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |\n"
                  " | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |\n"
                  " | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|\n"
                  "  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)\n"
                  "---------------------------------------------------------------------------------------------")
            quit(0)

    if command == 'help':
        print("---------------------------------------------------------------------------------------------\n"
              "Controls and Descriptions:"
              "t = take (an item)\n"
              "a = attack (if there's an enemy nearby)"
              "i = inventory (view items in your inventory)\n"
              "equipped = weapons equipped (weapons only)\n"
              "u = use (an item)\n"
              "l = look (for items in area)\n"
              "n, s, e, w = 'North', 'South', 'East', 'West' (for moving in directions + typing in the full word works "
              "too)\n "
              "---------------------------------------------------------------------------------------------\n"
              "To review these controls again type in 'help'\n"
              "---------------------------------------------------------------------------------------------")

    if command == 'equipped':
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
        print("What do you want to take? (Type in the item name with a capital.)")
        print("---------------------------------------------------------------------------------------------")
        item_requested = input(">_")
        found = False
        for item in current_node.roominv:
            if item.name == item_requested:
                player.inv.append(item)
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
    if command in 'l':
        print("---------------------------------------------------------------------------------------------")
        if len(current_node.roominv) > 0:
            print("Item(s) in your area:")
            for item in current_node.roominv:
                print(item.name)
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

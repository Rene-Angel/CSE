class Item(object):
    def __init__(self, name, price):
        self.name = name
        # self.armor = armor
        self.price = price


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
    def __init__(self, name, health, attack, stats, weapons, inv):
        self.name = name
        self.health = health
        self.stats = stats
        self.weapons = weapons
        self.inv = inv
        self.attack_amt = attack

    def attack(self, target):
        if target.damage(self.attack_amt):
            print("You took Damage.")

    def take_damage(self, dmg):
        self.health(dmg)


class Room(object):
    def __init__(self, name, north, south, east, west, items, character, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.items = items
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

player = Character(None, 500, 25, None, [ragnarok], [apple])
troll = Character("Troll", 150, 25, None, [trollaxe], [egg])
goblin = Character("Goblin", 100, 10, None, [dagger], [egg])
skeleton = Character("Skeleton", 75, 15, None, [sword], [None])
dragon = Character("Dragon", 1000, 45, None, [None], [None])
ghost = Character("Ghost", 50, 10, None, [None], [None])

hallway_1 = Room("Long Corridor", 'hallway_2', 'hallway_3', 'wall_opening', None,
                 [sword, waraxe], None, 'This long Hallway leads to: '
                                        'North: Long Corridor '
                                        'South: Long Corridor '
                                        'East: Broken Wall Opening ')
hallway_2 = Room("Long Corridor", 'hallway_6', 'hallway_1', None, 'broom_closet',
                 [apple, Sword], None, 'This Long Hallway leads to: '
                                       'North: Long Corridor '
                                       'South: Long Corridor '
                                       'East: '
                                       'West: ')
hallway_3 = Room("Long Corridor", 'hallway_1', None, 'hallway_4', None,
                 [None], None, 'This Long Hallway leads to: '
                               'North: Long Corridor '
                               'South: '
                               'East: Long Corridor '
                               'West: ')
hallway_4 = Room("Long Corridor", None, 'hallway_5', None, 'hallway_3',
                 [None], None, 'This Long Hallway leads to: '
                               'North: Long Corridor '
                               'South: '
                               'East: '
                               'West: Long Corridor ')
hallway_5 = Room("Long Corridor", 'hallway_4', 'hallway_6', None, None,
                 [None], None, 'This Long Hallway leads to: '
                               'North: Long Corridor '
                               'South: Long Corridor '
                               'East: '
                               'West: ')
hallway_6 = Room("Long Corridor", None, 'hallway_2', None, 'hallway_7',
                 [None], None, 'This Long Hallway leads to: '
                               'North: '
                               'South: Long Corridor '
                               'East: '
                               'West: Long Corridor ')
hallway_7 = Room("Long Corridor", None, None, 'hallway_6', 'hallway_8',
                 [None], None, 'This Long Hallway leads to: '
                               'North: '
                               'East: Long Corridor '
                               'West: Long Corridor ')
hallway_8 = Room("Long Corridor", None, None, 'hallway_7', 'hallway_9',
                 [None], None, 'This Long Hallway leads to: '
                               'North: '
                               'East: Long Corridor '
                               'West: Long Corridor ')
hallway_9 = Room("Long Corridor", None, None, 'hallway_8', 'hallway_10',
                 [None], None, 'This Long Hallway leads to: '
                               'North: '
                               'East: Long Corridor '
                               'West: Long Corridor ')
hallway_10 = Room("Long Corridor", None, None, 'hallway_9', None,
                  [None], None, 'This Long Hallway leads to: '
                                'North: '
                                'East: Long Corridor '
                                'West: ')
hallway_11 = Room("Long Corridor", None, None, None, None,
                  [None], None, 'This Long Hallway leads to: '
                                'North: '
                                'South: '
                                'East: ')
hallway_12 = Room("Long Corridor", None, None, 'hallway_24', 'hallway_13',
                  [None], None, 'This Long Hallway leads to: '
                                'South: '
                                'East: Long Corridor '
                                'West: Long Corridor ')
hallway_13 = Room("Long Corridor", 'hallway_14', None, 'hallway_18', 'hallway_12',
                  [None], None, 'This Long Hallway leads to: '
                                'North: Long Corridor '
                                'East: Long Corridor '
                                'West: Long Corridor ')
hallway_14 = Room("Long Corridor", 'hallway_15', 'hallway_13', None, None,
                  [None], None, 'This Long Hallway leads to: '
                                'North: Long Corridor '
                                'South: Long Corridor '
                                'East: ')
hallway_15 = Room("Long Corridor", 'hallway_17', 'hallway_14', None, None,  # Decided to Remove 'hallway_16' unnecessary
                  [None], None, 'This Long Hallway leads to: '
                                'North: Long Corridor '
                                'South: Long Corridor '
                                'East: '
                                'West: ')
hallway_17 = Room("Long Corridor", None, 'hallway_15', None, None,
                  [None], None, 'This Long Hallway leads to: '
                                'North: '
                                'South: Long Corridor '
                                'East: '
                                'West: ')
hallway_18 = Room("Long Corridor", None, None, 'hallway_13', 'hallway_20',  # Decided to remove 'hallway_19' unnecessary
                  [None], None, 'This Long Hallway leads to: '
                                'North: '
                                'South: '
                                'East: Long Corridor '
                                'West: Long Corridor ')
hallway_20 = Room("Long Corridor", None, None, 'hallway_18', 'hallway_21',
                  [None], None, 'This Long Hallway leads to: '
                                'North: '
                                'East: Long Corridor '
                                'West: Long Corridor ')
hallway_21 = Room("Long Corridor", None, None, 'hallway_20', 'hallway_23', [None], None, 'This Long Hallway leads to: '
                                                                                         'North: '
                                                                                         'South: '
                                                                                         'East: Long Corridor '
                                                                                         'West: Long Corridor ')
hallway_23 = Room("Long Corridor", None, None, None, 'hallway_23', [None], None, 'This Long Hallway leads to: '
                                                                                 'North: '
                                                                                 'East: '
                                                                                 'West: Long Corridor ')
hallway_24 = Room("Long Corridor", 'hallway_5', None, None, 'hallway_12', [None], None, 'This Long Hallway Leads to: '
                                                                                        'North: Long Corridor '
                                                                                        'West: Long Corridor ')
the_entrance = Room("The Entrance", None, 'empty_room', None, None, [sword], None,
                    'You enter a room through a ladder, from where the top leads to an abandoned subway tunnel... '
                    'But your mission is to investigate where this place leads and eliminate any threats. To the south '
                    'there is a hallway leading to a room.')
empty_room = Room("An Empty Room", 'the_entrance', 'leaking_room', None, None, None, None,
                  'There is nothing in here, but mops and brooms. The smell of sewer water makes you feel sick.')
leaking_room = Room("The Leaking Room", 'empty_room', None, None, 'wall_opening',
                    {None}, None,
                    'You find yourself in another room, there\'s a cold breeze from the giant hole in the west wall.'
                    'The other walls have water dripping from the sewer pipes.')
wall_opening = Room("Broken Wall Opening", None, None, 'leaking_room', 'hallway_1', None, None,
                    'You are inside an opening of a brick wall. The inside of the wall is filled with pipes. '
                    'It\'s a tight squeeze but at least the rats aren\'t crawling up your legs.')
broom_closet = Room("The Broom Closet", None, None, None, 'hallway_2', None, None,
                    'There\'s nothing in here, but mops and brooms. There is a smell of chemicals coming from '
                    'the sewer pipes.')
alchemy_lab = Room("Secret Alchemy Lab", None, 'library', None, None, [healthpotion], None,
                   'Many different types of ingredients surround you on shelves. '
                   '\'ThErE iS nO wAy OuT\', says a tall mysterious figure.')
guard_room = Room("The Guard's Room", None, None, None, None, [trollaxe], troll,
                  'There are various weapons scattered across the floor. The skeletons of dead guards are piled in the '
                  'corner. It seems that you are not alone in this room.')

inventory = {}
current_node = the_entrance
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
    elif command == 'i':
        if len(player.inv) > 0:
            print("You have the following items in your inventory: ")
            for item in player.inv:
                print(item.name)
        else:
            print("You have nothing in your inventory.")
    if 'take' in command:
        item_requested = command[5:]
        if item_requested in current_node.items:
            player.inv.append(item)
            for current_node.items in player.inv:
                print("You picked up %s." % item.name)
                print("You now have %s in your inventory." % item.name)

        # found = False
        # for item in current_node.items:
        #     if item.name == item_requested:
        #         player.inv.append(item)
        #         for items in player.inv:
        #             print("You take %s." % item_requested)
        #             print("You have %s in your inventory." % item.name)
        #             print()
        #         found = True
        #         current_node.items.remove(item)
else:
    print("Command Not Recognized.")

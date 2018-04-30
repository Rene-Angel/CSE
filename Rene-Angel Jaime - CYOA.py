import string
# import ...(statements)
# class definitions
# items first
# characters second
# rooms third
# instantiate classes
# controller


class Item(object):
    def __init__(self, name, attack, armor, weight, price):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price


class Weapon(Item):
    def __init__(self):
        super(Weapon, self).__init__(name, attack, armor, weight, price)


class Consumable(Item):
    def __init__(self, name, effect, price):
        super(Consumable, self).__init__(name, price)
        self.effect = effect


class sword(Weapon):
    def __init__(self):
        super(sword, self).__init__("Sword", 5, 10)


class troll_axe(Weapon):
    def __init__(self):
        super(troll_axe, self).__init__("Troll_Axe", 25, 15)


class war_axe(Weapon):
    def __init__(self):
        super(war_axe, self).__init__("War Axe", 15, 20)


class health_potion(Consumable):
    def __init__(self):
        super(health_potion, self).__init__("Health Potion", 100, 100)


class apple(Consumable):
    def __init__(self):
        super(apple, self).__init__("Apple", 5, 1)


class branch(Weapon):
    def __init__(self):
        super(branch, self).__init__("Tree Branch", 10, 1)


class dagger(Weapon):
    def __init__(self):
        super(dagger, self).__init__("Dagger", 15, 10)


class ragnarok(Weapon):
    def __init__(self):
        super(ragnarok, self).__init__("Ragnarok", 25, 50)


class egg(Consumable):
    def __init__(self):
        super(egg, self).__init__("Egg", 10, 5)


class stick(Weapon):
    def __init__(self):
        super(stick, self).__init__("Stick", 1, 1)


# sword = sword()
# dagger = dagger()
# egg = egg()
# apple = apple()
# trollaxe = troll_axe()
# waraxe = war_axe()
# stick = stick()
# health_potion = health_potion()
# ragnarok = ragnarok()
# branch = branch()


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


player = Character(None, 500, 25, None, ragnarok)
troll = Character("Troll", 150, 25, None, troll_axe)
goblin = Character("Goblin", 100, 10, None, dagger)
skeleton = Character("Skeleton", 75, 15, None, sword)
dragon = Character("Dragon", 1000, 45, None, None)
ghost = Character("Ghost", 50, 10, None, None)


class Room(object):
    def __init__(self, name, north, south, east, west, items, character, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.items = items()
        self.character = character

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


hallway_1 = Room("Long Corridor", 'hallway_2', 'hallway_3', 'wall_opening', None,
                 Item[ragnarok, war_axe], None, 'This long Hallway leads to: '
                                                'North: Long Corridor '
                                                'South: Long Corridor '
                                                'East: Broken Wall Opening ')
hallway_2 = Room("Long Corridor", 'hallway_6', 'hallway_1', None, 'broom_closet',
                 Item[apple, sword], None, 'This Long Hallway leads to: '
                                           'North: Long Corridor '
                                           'South: Long Corridor '
                                           'East: '
                                           'West: ')
hallway_3 = Room("Long Corridor", 'hallway_1', None, 'hallway_4', None,
                 None, None, 'This Long Hallway leads to: '
                             'North: Long Corridor '
                             'South: '
                             'East: Long Corridor '
                             'West: ')
hallway_4 = Room("Long Corridor", None, 'hallway_5', None, 'hallway_3',
                 None, None, 'This Long Hallway leads to: '
                             'North: Long Corridor '
                             'South: '
                             'East: '
                             'West: Long Corridor ')
hallway_5 = Room("Long Corridor", 'hallway_4', 'hallway_6', None, None,
                 None, None, 'This Long Hallway leads to: '
                             'North: Long Corridor '
                             'South: Long Corridor '
                             'East: '
                             'West: ')
hallway_6 = Room("Long Corridor", None, 'hallway_2', None, 'hallway_7',
                 None, None, 'This Long Hallway leads to: '
                             'North: '
                             'South: Long Corridor '
                             'East: '
                             'West: Long Corridor ')
hallway_7 = Room("Long Corridor", None, None, 'hallway_6', 'hallway_8',
                 None, None, 'This Long Hallway leads to: '
                             'North: '
                             'East: Long Corridor '
                             'West: Long Corridor ')
hallway_8 = Room("Long Corridor", None, None, 'hallway_7', 'hallway_9',
                 None, None, 'This Long Hallway leads to: '
                             'North: '
                             'East: Long Corridor '
                             'West: Long Corridor ')
hallway_9 = Room("Long Corridor", None, None, 'hallway_8', 'hallway_10',
                 None, None, 'This Long Hallway leads to: '
                             'North: '
                             'East: Long Corridor '
                             'West: Long Corridor ')
hallway_10 = Room("Long Corridor", None, None, 'hallway_9', None,
                  None, None, 'This Long Hallway leads to: '
                              'North: '
                              'East: Long Corridor '
                              'West: ')
hallway_11 = Room("Long Corridor", None, None, None, None,
                  None, None, 'This Long Hallway leads to: '
                              'North: '
                              'South: '
                              'East: ')
hallway_12 = Room("Long Corridor", None, None, 'hallway_24', 'hallway_13',
                  None, None, 'This Long Hallway leads to: '
                              'South: '
                              'East: Long Corridor '
                              'West: Long Corridor ')
hallway_13 = Room("Long Corridor", 'hallway_14', None, 'hallway_18', 'hallway_12',
                  None, None, 'This Long Hallway leads to: '
                              'North: Long Corridor '
                              'East: Long Corridor '
                              'West: Long Corridor ')
hallway_14 = Room("Long Corridor", 'hallway_15', 'hallway_13', None, None,
                  None, None, 'This Long Hallway leads to: '
                              'North: Long Corridor '
                              'South: Long Corridor '
                              'East: ')
hallway_15 = Room("Long Corridor", 'hallway_17', 'hallway_14', None, None,  # Decided to Remove 'hallway_16' unnecessary
                  None, None, 'This Long Hallway leads to: '
                              'North: Long Corridor '
                              'South: Long Corridor '
                              'East: '
                              'West: ')
hallway_17 = Room("Long Corridor", None, 'hallway_15', None, None,
                  None, None, 'This Long Hallway leads to: '
                              'North: '
                              'South: Long Corridor '
                              'East: '
                              'West: ')
hallway_18 = Room("Long Corridor", None, None, 'hallway_13', 'hallway_20',  # Decided to remove 'hallway_19' unnecessary
                  None, None, 'This Long Hallway leads to: '
                              'North: '
                              'South: '
                              'East: Long Corridor '
                              'West: Long Corridor ')
hallway_20 = Room("Long Corridor", None, None, 'hallway_18', 'hallway_21',
                  None, None, 'This Long Hallway leads to: '
                              'North: '
                              'East: Long Corridor '
                              'West: Long Corridor ')
hallway_21 = Room("Long Corridor", None, None, 'hallway_20', 'hallway_23', None, None, 'This Long Hallway leads to: '
                                                                                       'North: '
                                                                                       'South: '
                                                                                       'East: Long Corridor '
                                                                                       'West: Long Corridor ')
hallway_23 = Room("Long Corridor", None, None, None, 'hallway_23', None, None, 'This Long Hallway leads to: '
                                                                               'North: '
                                                                               'East: '
                                                                               'West: Long Corridor ')
hallway_24 = Room("Long Corridor", 'hallway_5', None, None, 'hallway_12', None, None, 'This Long Hallway Leads to: '
                                                                                      'North: Long Corridor '
                                                                                      'West: Long Corridor ')
the_entrance = Room("The Entrance", None, 'empty_room', None, None, Item[sword], None,
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
alchemy_lab = Room("Secret Alchemy Lab", None, 'library', None, None, Item[health_potion], None,
                   'Many different types of ingredients surround you on shelves. '
                   '\'ThErE iS nO wAy OuT\', says a tall mysterious figure.')
guard_room = Room("The Guard's Room", None, None, None, None, Item[sword], troll,
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
        try:
            for item in items.values():
                print('\t'.join([str(x) for x in [item.name]]))
        except KeyError:
            print("There's Nothing in your inventory.")
            print()
        # for item in inventory:
        #     print(item)
        # else KeyError:
        #     print("Nothing in your inventory")
    elif command == 't':
        try:
            print("What do you want to take?")
            input()
            if input == current_node.items:
                items[item.name] = current_item
                inventory.append(current_item)
            # print("What do you want to take?")
        except KeyError:
            print("Nothing here to take.")
            print("")
    else:
        print("Command Not Recognized.")
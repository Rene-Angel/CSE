# import ...(statements)
# class definitions
# items first
# characters second
# rooms third
# instantiate classes
# controller


class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.take = True
        self.drop = False
        self.health = 1000
        self.target_health = 1000

    def discard(self):
        self.take = False
        self.drop = True
        print("You dropped %s." % self.name)

    def obtain(self):
        self.take = True
        self.drop = False
        print("You obtained %s." % self.name)

    def sell(self):
        self.value += 100


class Weapon(Item):
    def __init__(self, name, attack, value):
        super(Weapon, self).__init__(name, value)
        self.attack = attack

    def attack(self):
        self.attack = True
        self.target_health -= self.attack


class Ammunition(Item):
    def __init__(self, name, damage, amount):
        super(Ammunition, self).__init__(name, value)
        self.damage = damage
        self.amount = amount

    def fire(self):
        self.target_health -= self.damage


class Consumable(Item):
    def __init__(self, name, effect, value):
        super(Consumable, self).__init__(name, value)
        self.use = False
        self.effect = effect

    def use(self):
        self.use = True
        print("You used this item")
        self.health += self.effect
        self.effect = True


class Bone_Sword(Weapon):
    def __init__(self):
        super(Bone_Sword, self).__init__("Bone Sword", 5, 10)


class War_Axe(Weapon):
    def __init__(self):
        super(War_Axe, self).__init__("War Axe", 15, 20)


class X_Bow(Weapon):
    def __init__(self):
        super(X_Bow, self).__init__("Cross Bow", 20, 40)


class Arrows(Ammunition):
    def __init__(self):
        super(Arrows, self).__init__("Arrows", 25, 50)


class Health_Potion(Consumable):
    def __init__(self):
        super(Health_Potion, self).__init__("Health Potion", 100, 100)


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


class Long_Bow(Ammunition):
    def __init__(self):
        super(Long_Bow, self).__init__("Long Bow", 20, 30)


class Stick(Item):
    def __init__(self):
        super(Stick, self).__init__("Stick", 0)

    def interact(self):
        print("What more do you want its just a stick.")


class Super_Stick(Stick):
    def __init__(self):
        super(Super_Stick, self).__init__("Super Stick", 0)


class Character(object):
    def __init__(self, name, health, attack, stats, inventory):
        self.name = name
        self.health = health
        self.stats = stats
        self.inventory = inventory
        self.attack_amt = attack

    def attack(self, target):
        if target.damage(self.attack_amt):
            print("You took Damage.")

    def take_damage(self, dmg):
        self.health(dmg)


player = Character("Rodin", 500, 25, None, 'Ragnarok')


class Room(object):
    def __init__(self, name, north, south, east, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
# west_house = Room("West of House", 'north_house', None, None, None, "This is the West side of the House.")
# Information = ( Name, North, South, East, West, Description )
hallway_1 = Room("Long Corridor", 'hallway_2', 'hallway_3', 'wall_opening', None,
                 "This long Hallway leads to: "
                 "North: Long Corridor "
                 "South: Long Corridor "
                 "East: Broken Wall Opening ")
hallway_2 = Room("Long Corridor", 'hallway_6', 'hallway_1', None, 'broom_closet',
                 "This Long Hallway leads to: "
                 "North: Long Corridor "
                 "South: Long Corridor "
                 "East: "
                 "West: ")
hallway_3 = Room("Long Corridor", 'hallway_1', None, 'hallway_4', None,
                 "This Long Hallway leads to: "
                 "North: Long Corridor "
                 "South: "
                 "East: Long Corridor "
                 "West: ")
hallway_4 = Room("Long Corridor", None, 'hallway_5', None, 'hallway_3',
                 "This Long Hallway leads to: "
                 "North: Long Corridor "
                 "South: "
                 "East: "
                 "West: Long Corridor ")
hallway_5 = Room("Long Corridor", 'hallway_4', 'hallway_6', None, None,
                 "This Long Hallway leads to: "
                 "North: Long Corridor "
                 "South: Long Corridor "
                 "East: "
                 "West: ")
hallway_6 = Room("Long Corridor", None, 'hallway_2', None, 'hallway_7',
                 "This Long Hallway leads to: "
                 "North: "
                 "South: Long Corridor "
                 "East: "
                 "West: Long Corridor ")
hallway_7 = Room("Long Corridor", None, None, 'hallway_6', 'hallway_8',
                 "This Long Hallway leads to: "
                 "North: "
                 "East: Long Corridor "
                 "West: Long Corridor ")
hallway_8 = Room("Long Corridor", None, None, 'hallway_7', 'hallway_9',
                 "This Long Hallway leads to: "
                 "North: "
                 "East: Long Corridor "
                 "West: Long Corridor ")
hallway_9 = Room("Long Corridor", None, None, 'hallway_8', 'hallway_10',
                 "This Long Hallway leads to: "
                 "North: "
                 "East: Long Corridor "
                 "West: Long Corridor ")
hallway_10 = Room("Long Corridor", None, None, 'hallway_9', None,
                  "This Long Hallway leads to: "
                  "North: "
                  "East: Long Corridor "
                  "West: ")
hallway_11 = Room("Long Corridor", None, None, None, None,
                  "This Long Hallway leads to: "
                  "North: "
                  "South: "
                  "East: ")
hallway_12 = Room("Long Corridor", None, None, 'hallway_24', 'hallway_13',
                  "This Long Hallway leads to: "
                  "South: "
                  "East: Long Corridor "
                  "West: Long Corridor ")
hallway_13 = Room("Long Corridor", 'hallway_14', None, 'hallway_18', 'hallway_12',
                  "This Long Hallway leads to: "
                  "North: Long Corridor "
                  "East: Long Corridor "
                  "West: Long Corridor ")
hallway_14 = Room("Long Corridor", 'hallway_15', 'hallway_13', None, None,
                  "This Long Hallway leads to: "
                  "North: Long Corridor "
                  "South: Long Corridor "
                  "East: ")
hallway_15 = Room("Long Corridor", 'hallway_17', 'hallway_14', None, None,  # Decided to Remove 'hallway_16' unnecessary
                  "This Long Hallway leads to: "
                  "North: Long Corridor "
                  "South: Long Corridor "
                  "East: "
                  "West: ")
hallway_17 = Room("Long Corridor", None, 'hallway_15', None, None,
                  "This Long Hallway leads to: "
                  "North: "
                  "South: Long Corridor "
                  "East: "
                  "West: ")
hallway_18 = Room("Long Corridor", None, None, 'hallway_13', 'hallway_20',  # Decided to remove 'hallway_19' unnecessary
                  "This Long Hallway leads to: "
                  "North: "
                  "South: "
                  "East: Long Corridor "
                  "West: Long Corridor ")
hallway_20 = Room("Long Corridor", None, None, 'hallway_18', 'hallway_21',
                  "This Long Hallway leads to: "
                  "North: "
                  "East: Long Corridor "
                  "West: Long Corridor ")
hallway_21 = Room("Long Corridor", None, None, 'hallway_20', 'hallway_23',  # Decided to Remove 'hallway_22'
                  "This Long Hallway leads to: "
                  "North: "
                  "South: "
                  "East: Long Corridor "
                  "West: Long Corridor ")
hallway_23 = Room("Long Corridor", None, None, None, 'hallway_23',
                  "This Long Hallway leads to: "
                  "North: "
                  "East: "
                  "West: Long Corridor ")
hallway_24 = Room("Long Corridor", 'hallway_5', None, None, 'hallway_12',
                  "This Long Hallway Leads to: "
                  "North: Long Corridor "
                  "West: Long Corridor ")
the_entrance = Room("The Entrance", None, 'empty_room', None, None,
                    "You enter a room through a ladder, from where the top leads to an abandoned subway tunnel... "
                    "But your mission is to investigate where this place leads and eliminate any threats. To the south "
                    "there is a hallway leading to a room.")
empty_room = Room("An Empty Room", 'the_entrance', 'leaking_room', None, None,
                  "There is nothing in here, but mops and brooms. The smell of sewer water makes you feel sick.")
leaking_room = Room("The Leaking Room", 'empty_room', None, None, 'wall_opening',
                    "You find yourself in another room, there's a cold breeze from the giant hole in the west wall."
                    "The other walls have water dripping from the sewer pipes.")
wall_opening = Room("Broken Wall Opening", None, None, 'leaking_room', 'hallway_1',
                    "You are inside an opening of a brick wall. The inside of the wall is filled with pipes. "
                    "It's a tight squeeze but at least the rats aren't crawling up your legs.")
broom_closet = Room("The Broom Closet", None, None, None, 'hallway_2',
                    "There's nothing in here, but mops and brooms. There is a smell of chemicals coming from "
                    "the sewer pipes.")
# alchemy_lab = Room("Secret Alchemy Lab", )


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
        # look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
            print("")
    else:
        print('Command not Recognized')

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
                    "There's nothing in here, but mops and brooms. There is though a smell of chemicals coming form "
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

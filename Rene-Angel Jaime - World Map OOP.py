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
                    "You are inside an opening of a brick wall, it's a tight squeeze but at least the rats aren't "
                    "crawling up your legs.")
broom_closet = Room("The Broom Closet", None, None, None, 'hallway_1',
                    "There's nothing in here, but mops and brooms. There is though a smell of chemicals coming form "
                    "the sewer pipes.")

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
            name_of_node = current_node[command]
            current_node = Room[name_of_node]
        except KeyError:
            print("You cannot go this way.")
            print("")
    else:
        print('Command not Recognized')

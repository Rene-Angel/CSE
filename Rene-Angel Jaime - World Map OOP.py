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
the_entrance = Room("The Entrance", None, 'leaking_room', "You enter a room through a ladder, from where the top leads to an abandoned subway tunnel..."
                       "But your mission is to investigate where this place leads and eliminate any threats."
                       "To the south there is a hallway leading to a room.
dungeon_map = {
    'START': {
        'NAME': "The Entrance",
        'DESCRIPTION': "You enter a room through a ladder, from where the top leads to an abandoned subway tunnel..."
                       "But your mission is to investigate where this place leads and eliminate any threats."
                       "To the south there is a hallway leading to a room.",
        'PATHS': {
            'SOUTH': 'R2'
        }
    },
    'R2': {
        'NAME': "An Empty Room",
        'DESCRIPTION': "The smell of sewer water is disgusting.",
        'PATHS': {
            'NORTH': 'START',
            'SOUTH': 'R3'
        }
    },
    'R3': {
        'NAME': "The Leaking Room",
        'DESCRIPTION': "You find yourself in another room, there's a cold breeze from the giant hole in the west wall."
                       "The other walls have water dripping from the sewer pipes.",
        'PATHS': {
            'WEST': 'R4',
            'NORTH': 'R2'
        }
    },
    'R4': {
        'NAME': "Broken Wall Opening",
        'DESCRIPTION': "You are inside an opening of a brick wall, it's a tight squeeze but at least the rights aren't "
                       "crawling up your legs.",
        'PATHS': {
            'WEST': 'H1',
            'EAST': 'R3'
        }
    },
    'R5': {
        'NAME': "The Broom Closet",
        'DESCRIPTION': "There's nothing in here, but mops and brooms. There is though a smell of chemicals coming form "
                       "the sewer pipes.",
        'PATHS': {
            'WEST': 'H1'
        }
    },
    'R6': {
        'NAME': "Secret Alchemy Lab",
        'DESCRIPTION': "There are many chemicals around you, along with the strange ingredients found in bookshelves "
                       "of recipes and jars of dragon eyes.",
        'PATHS': {
            'SOUTH': 'R50'
        }
    },
    'R7': {
        'NAME': "The Dark Room",
        'DESCRIPTION': "You are likely to be killed in a suspicous rrom like this you'll need some light if you are "
                       "willing to see clearly",
        'PATHS': {
            'SOUTH': 'H2'
        }
    },
    'R8': {
        'NAME': "The Training Room",
        'DESCRIPTION': "There's a mat on the floor for martial arts and sword practice, along with the skeletons of "
                       "the dead still holding their katanas.",
        'PATHS': {
            'SOUTH': 'H2'
        }
    },
    'R9': {
        'NAME': "The Shrine Room",
        'DESCRIPTION': "A space lit with candles on the north side of the room, and a large painting hanging on the "
                       "wall. There's a slight breeze in the room.",
        'PATHS': {
            'NORTH': 'R46',
            'SOUTH': 'H2'
        }
    },
    'R10': {
        'NAME': "The Guard's Restroom",
        'DESCRIPTION': "The room's a mess, and has a horrible stench.",
        'PATHS': {
            'WEST': 'R11'
        }
    },
    'R11': {
        'NAME': "The Guard's Base",
        'DESCRIPTION': "A table pierced with knives and ancient writing stands in the middle of the room, along with a "
                       "map. This is probably where they gave out missions for them to do.",
        'PATHS': {
            'WEST': 'H9',
            'E1': 'H2',
            'E2': 'R10'
        }
    },
    'R12': {
        'NAME': "The Dragon's Keep",
        'DESCRIPTION': "There is a large pile of bones and ashes leading many feet high, but at the top of that pile "
                       "you find a sleeping dragon awaken from it's slumber.",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'R13': {
        'NAME': "The Library",
        'DESCRIPTION': "The room where the ancient ones used to read and research such forbidden knowledge.",
        'PATHS': {
            'NORTH': 'R6',
            'SOUTH': 'H2'
        }
    },
    'INTERSECTION': {
        'NAME': "Intersection",
        'DESCRIPTION': "You find yourself in and intersection between halls.",
        'PATHS': {
            'NORTH': 'H7',
            'WEST': 'H6',
            'EAST': 'H5'
        }
    },
    'H1': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "This long Hallway leads to: "
                       "North: Long Corridor "
                       "South: Long Corridor "
                       "East: Broken Wall Opening ",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H2': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H3': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H4': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H5': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H6': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H7': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H8': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'H9': {
        'NAME': "Long Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': ''
        }
    },
}

current_node = dungeon_map['START']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    print("")
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = dungeon_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
            print("")
    else:
        print('Command not Recognized')

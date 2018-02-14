dungeon_map = {
    'SUBWAYLADDER': {
        'NAME': "Subway Ladder",
        'DESCRIPTION': "You are west of a white house",
        'PATHS':{
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': "You are south of a white house",
        'PATHS':{
           'NORTH': 'WESTHOUSE'
        }
    }
}

current_node = dungeon_map['SUBWAYLADDER']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        name_of_node = current_node['PATHS'][command]
        current_node = dungeon_map[name_of_node]
    else:
        print('Command not Recognized')
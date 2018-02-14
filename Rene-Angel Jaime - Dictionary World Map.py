world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of a white house",
        'PATHS':{
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': "North of House",
        'DESCRIPTION': "You are north of a white house",
        'PATHS':{
            'SOUTH': 'WESTHHOUSE'
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

current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHWEST', 'NORTHEAST', 'SOUTHWEST', 'SOUTHEAST']

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
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
            print("")
    else:
        print('Command not Recognized')
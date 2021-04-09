#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''RPG Game ======== Commands:
     go [direction] 
     get [item] 
     observe (observe the current room and lets you know which directions you can go)
     help (displays command list) 
     It would be best if you observe first in every room
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'armory': {
        'south': 'war room',
        'east': 'barracks',
        'north': 'north room',
        'item': 'key',
        'description': '''The Armory is were all of the weapons are kept. From this room you can go south to the War 
        Room, east to the Barracks, or North to the North Room. There is a key in this room if you have not already 
        found it. I would stay away from the War Room if I were you. Or go to the North Room and get the sword before 
        you go to the War Room. I know it is ironic that the armory doesn't have the weapon you need. '''
    },

    'war room': {
        'north': 'armory',
        'east': 'courtyard',
        'item': 'monster',
        'description': ' you bout to die',
    },
    'barracks': {
        'west': 'armory',
        'south': 'courtyard',
        'item': 'potion',
        'north': 'kitchen',
        'description': 'The Barracks is were all of the troops sleep. There also are various shenanigans that are '
                       'played here so be on the look out. From this room you can go west to the armory, south to the '
                       ' Courtyard, or north to the Kitchen. There is an item here if you have not already seen it '
    },
    'courtyard': {
        'north': 'barracks',
        'west': 'War Room',
        'item': 'betrayal',
        'description': '''The Courtyard is kind of like the Rose Garden in  Game of Thrones. Whatever you do, 
        don't pick up the betrayal. From this room you can go west to the War Room or North to the Barracks '''
    },
    'kitchen': {
        'south': 'barracks',
        'west:' 'north Room'
        'item': 'cookie',
        'description': '''The Kitchen is were all the foods is prepared. I think there is a cookie for you to try. 
        From this room you can go west to the North Room or south to the Barracks '''
    },
    'north room': {
        'south': 'armory',
        'east': 'kitchen',
        'item': 'sword',
        'description': '''The North Room got its name for a reason. It also has a secret weapons stash. You might 
        want to grab the Sword before you go into the War Room.From this room you can go south to the Armory or east 
        to the Kitchen '''

    }
}

# start the player in the Armory
currentRoom = 'armory'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # this gives description of the room.
    if move[0] == 'observe':
        print(str(rooms[currentRoom]['description']))

    # this gives the player the option to quit
    if move[0] == 'quit':
        while True:
            quitter = input('Are you sure you want to quit: ')
            if quitter.lower() == 'no':
                print('good, lets continue')
                break
            elif quitter.lower() != 'yes':
                print(" You must have made a mistake because you didn't say yes or no ")
            else:
                exit()
    # this gives the player a directions/help
    if move[0] == 'help':
        showInstructions()

    # Define how a player can win
    if currentRoom == 'courtyard' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    # Courtyard betrayal
    elif 'betrayal' in inventory:
        print(' You were warned. You have been betrayal in the Rose Garden. I mean Courtyard')
        break
    # kitchen quiz
    elif currentRoom == 'kitchen':
        print ('''You have entered the quiz kitchen. If you answer all of the questions correctly, you will get to 
        leave this place. If not, well have you seen any of the SAW movies. Its best that you get these questions 
        right ''')
        answer1 = input('Who is the the Sixth Hokage?   :')
        answer2 = int(input('How many tails does the fox inside Naruto have? '))
        answer3 = int(input('This is the final question. How much wood would a woodchuck chuck if a woodchuck could '
                            'chuck wood? '))

        if answer1.lower() == 'kakashi hatake ' and answer2 == 9 and answer3 == 7:
            print("You passed this time, next time you might not be so lucky")
            break
        else:
            print("You fail and its time for that stuff that happens in the SAW movies so I gotta run. Have fun "
                  "slowly dying.")
            exit()
    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        # if the player has a sword they win
        if 'sword' in inventory:
            print('Good thing you go that sword there was a monster but you killed him.')
            print ('You have won and my exit the building. Next time don\'t go in random buildings.')
            break
        # if the player does not have the sword they lose
        else:
            print('A monster has got you... GAME OVER!')
            break

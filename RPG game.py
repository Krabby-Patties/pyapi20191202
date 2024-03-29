#!/usr/bin/bash

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
    ''')

def showStatus():
    #print the player's current status
    print('----------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' +str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("-------------------------")

#an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen'
    },
    'Kitchen' : {
        'north' : 'Hall'
        }
    }
#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

    showStatus()

    #get the players next 'move'
    #.split() breaks it up into a list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ",1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
        #there is no door (link) to the new room
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You cant\'t go that way!')

     #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message  print(move[1]]
            print(move[1] + 'got!')
            #delete the item from the room
            del rooms[currentRoom]['item']

         #otherwise if the item isnt there to get
        else:
            #tell them they cant get it
            print('Can\'t get ' + move[1] + '!')
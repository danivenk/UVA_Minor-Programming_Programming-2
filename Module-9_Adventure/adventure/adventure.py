#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
adventure.py lets you play a game of adventure
    used together with room.py and item.py
Dani van Enk, 11823526
"""

# import room and item files
from room import Room
from item import Item


class Adventure():
    """
    adventure class defines a game of adventure

    methods:
    load_rooms              - loads rooms form filename
    get_description         - description of current room
    get_long_description    - long description of current room
    move                    - move to specified room
    is_forced               - check if forced exsits
    get_items               - gets items in current room
    add_to_inventory        - add item to inventory
    del_from_inventory      - remove item from inventory
    get_inventory           - gets inventory
    """

    def __init__(self, game):
        """
        initializes the adventure class

        parameter:
        game - type of game to play
        """

        # room dictionary init in following format {roomnumber:Room}
        self.rooms = {}

        # inventory dictionary init in following format {"item_name":Item}
        self.inventory = {}

        # Load room structures
        self.load_rooms(f"data/{game}Adv.dat")

        # make sure room 1 is in room and set that as current room
        assert 1 in self.rooms
        self.current_room = self.rooms[1]

    def load_rooms(self, filename):
        """
        loads rooms from filename

        parameter:
        filename - file to load rooms from
        """

        # open file
        file = open(filename, "r")

        # read first paragraph
        line = file.readline()
        while (line != "\n"):
            
            # create list of data in line
            line_data = line.strip("\n").split("\t")

            # create room
            self.rooms[int(line_data[0])] = \
                Room(int(line_data[0]), line_data[1], line_data[2])

            line = file.readline()

        # read second paragraph
        line = file.readline()
        while (line != "\n"):

            # create list of data in line
            line_data = line.strip("\n").split("\t")

            # room number of editing room, first in line_data
            editing_room_no = int(line_data[0])

            # loop over direction room pairs and add connections to rooms
            for data in range(1, len(line_data), 2):

                # check for conditional room
                if "/" in line_data[data + 1]:
                    conditional_room = line_data[data + 1].split("/")
                    self.rooms[editing_room_no].add_connection(line_data[data], \
                        self.rooms[int(conditional_room[0])], conditional_room[1])
                else:
                    self.rooms[editing_room_no].add_connection(line_data[data], \
                        self.rooms[int(line_data[data + 1])])

            line = file.readline()

        # read last paragraph
        line = file.readline()
        while (line != ""):

            # create list of data in line
            line_data = line.strip("\n").split("\t")

            # create item
            new_item = Item(line_data[0], line_data[1])

            # add to room
            self.rooms[int(line_data[2])].add_item(new_item, line_data[0])

            line = file.readline()

        # close file
        file.close()

    def get_description(self):
        """
        gets description of current room
            short description if visited, long if not
        
        returns description
        """

        if self.current_room.get_visited():
            return self.current_room.get_name()
        else:
            return self.current_room.get_description()

    def get_long_description(self):
        """
        returns long description
        """

        return self.current_room.get_description()

    def move(self, direction):
        """
        moves to a different room

        parameter:
        direction - direction to move to

        return True if move has succeeded, False if not
        """

        # return false for non-existant directions 
        if not self.current_room.has_connection(direction):
            return False

        # set visited True if not already true
        if not self.current_room.get_visited():
            self.current_room.set_visited()

        # get room to move to
        move_room = self.current_room.get_connection(direction)

        # check if there is a conditional movement in the direction
        for item in self.inventory:
            if item in move_room:
                self.current_room = move_room[item]
                return True

        # move to standard room if not
        self.current_room = move_room[""]

        return True

    def is_forced(self):
        """
        checks for forced movement

        returns true if forced movement has been found, else false
        """

        if self.current_room.has_connection("forced"):
            return True

        return False

    def get_items(self):
        """
        returns items in current room
        """

        return self.current_room.get_items()
    
    def add_to_inventory(self, item_name):
        """
        add item to inventory

        parameter:
        item_name - name of item to be added

        returns true if this succeeded, false if not
        """
        
        # get item from room
        pickup_item = self.current_room.pick_up_item(item_name)

        # if found add to inventory
        if pickup_item != None:
            self.inventory[item_name] = pickup_item
            return True

        return False
    
    def del_from_inventory(self, item_name):
        """
        remove item from inventory

        parameter:
        item_name - name of item to be removed

        returns true if succeeded, false if not
        """

        # remove item to inventory
        if item_name in self.inventory:
            self.current_room.add_item(self.inventory.pop(item_name), item_name)
            return True
        
        return False

    def get_inventory(self):
        """
        returns inventory
        """

        return self.inventory


def get_synonyms():
    """
    creates a synonym dictionary

    returns synonym dictionary
    """

    # open synonym file
    with open("data/Synonyms.dat") as file:

        # create synonym dictionary in following format {"synonym":"command"}
        synonyms_dict = {}

        # add each synonym to the dictionary
        for line in file:
            line = line.lower().strip("\n")
            synonyms = line.split("=")

            synonyms_dict[synonyms[0]] = synonyms[1]

        return synonyms_dict


# run program
if __name__ == "__main__":
    
    # import library
    from sys import argv

    # Check command line arguments
    if len(argv) not in [1,2]:
        print("Usage: python adventure.py [name]")
        exit(1)

    # Load the requested game or else Tiny
    if len(argv) == 1:
        game_name = "Tiny"
    elif len(argv) == 2:
        game_name = argv[1]

    # Create game
    adventure = Adventure(game_name)

    # get synonyms
    synonyms = get_synonyms()

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.get_description())

    # print items in room if any
    for item in adventure.get_items().values():
        print(item)

    # Prompt the user for commands until they type QUIT
    while True:

        # Prompt
        command = input("> ").lower()

        # set split command to false
        split = False

        # split command if it includes spaces into command an parameter
        if " " in command:
            commands = command.split(" ")
            command = commands.pop(0)
            parameter = commands
            split = True

        # check if command is a synonym
        if command in synonyms:
            command = synonyms[command]

        # quit program
        if command == "quit":
            break

        # print help statement
        elif command == "help":
            print("You can move by typing directions such as EAST/WEST/IN/OUT")
            print("QUIT quits the game.")
            print("HELP prints instructions for the game.")
            print("INVENTORY lists the item in your inventory.")
            print("LOOK lists the complete description of the room and" + \
                    "its contents.")
            print("TAKE <item> take item from the room.")
            print("DROP <item> drop item from your inventory.")

        # print long description and items
        elif command == "look":
            print(adventure.get_long_description())

            # print items in room if any
            for item in adventure.get_items().values():
                print(item)
        
        # pick up specified item
        elif command == "take":

            # if no parameters given invalid
            if not split:
                print("Invalid command")
                continue

            # if not an item invalid
            elif not adventure.add_to_inventory(parameter[0]) or \
                    len(parameter) != 1:
                print("No such item.")
                continue

            # print if success
            print(f"{parameter[0].upper()} taken.")

        # drop specified item
        elif command == "drop":

            # if no parameters given invalid
            if not split:
                print("Invalid command")
                continue

            # if not an item invalid
            elif not adventure.del_from_inventory(parameter[0]) or \
                    len(parameter) != 1:
                print("No such item.")
                continue

            # print if success
            print(f"{parameter[0].upper()} dropped.")

        # print items in inventory
        elif command == "inventory":

            # get items in inventory
            inventory = adventure.get_inventory()

            # print if items in inventory
            if len(inventory) > 0:
                for item in inventory.values():
                    print(item)
                continue

            # print if inventory is empty
            print("Your inventory is empty.")

        # move to specified direction
        else:

            # if no such direction connection invalid
            if not adventure.move(command):
                print("Invalid command")
                continue

            # print description and items if any present
            print(adventure.get_description())
            for item in adventure.get_items().values():
                print(item)

            # move forced if necessary
            while adventure.is_forced():
                adventure.move("forced")
                print(adventure.get_description())


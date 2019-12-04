#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
room.py defines the room class
Dani van Enk, 11823526
"""

class Room(object):
    """
    the room class defines a room which has connections to other rooms
        and has items

    sub-class -> object
    """

    def __init__(self, room_id, name, description):
        """
        initializes the room class

        parameters:
        room_id - the room number of the room;
        name - name of the room
        description - description of the room
        """

        # connection and item dictionaries
        self.connections = {}
        self.items = {}

        # Room properties
        self.id = room_id
        self.name = name
        self.description = description
        self.visited = False

    def get_name(self):
        """
        returns the name of the room
        """

        return self.name

    def get_description(self):
        """
        returns the room description
        """
        
        return self.description

    def add_connection(self, direction, room, condition=""):
        """
        adds an connection to the room

        parameters:
        direction - direction of the the connected room;
        room - the connected room;
        condition - condition to enter this connection (default is "")
        """

        # make sure condition and direction are lowercases
        direction = direction.lower()
        condition = condition.lower()

        # add connection accordingly
        if direction in self.connections:
            self.connections[direction][condition] = room
        else:
            self.connections[direction] = {}
            self.connections[direction][condition] = room

    def has_connection(self, direction):
        """
        checks is connection for given direction exists

        pratameter:
        direction - direction where to check connection for

        returns True if connection has been found else it returns False
        """

        # make sure direction is lowercase
        direction = direction.lower()

        # check if direction exists
        if direction in self.connections:
            return True
        else:
            return False

    def get_connection(self, direction):
        """
        get connected room for the given direction

        parameter:
        direction - direction to get room in

        returns connected room for the given direction
        """

        # make sure direction is lowercase
        direction = direction.lower()

        return self.connections[direction]

    def set_visited(self):
        """
        sets visited to True
        """

        self.visited = True

    def get_visited(self):
        """
        returns visited
        """

        return self.visited

    def add_item(self, item, item_name):
        """
        add item to room

        parameters:
        item - item to add to room
        item_name - name of item to add to room
        """
        
        # make sure item_name is lowercase
        item_name = item_name.lower()

        self.items[item_name] = item
    
    def get_items(self):
        """
        returns items in room
        """

        return self.items

    def pick_up_item(self, item_name):
        """
        remove item (pick up) from room

        parameter:
        item_name - name of item to pick up

        return item, if not found return None
        """
        
        # make sure item_name is lowercase
        item_name = item_name.lower()

        # find item
        if item_name in self.items:
                return self.items.pop(item_name)
    
        return None
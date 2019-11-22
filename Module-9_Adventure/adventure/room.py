class Room(object):

    # Initializes a Room
    def __init__(self, id, name, description):

        # Dictionary that maps directions like "EAST" to other room objects
        self.connections = {}

        # Room properties
        self.id = id
        self.name = name
        self.description = description

    # Adds a given direction and the connected room to our room object.
    def add_connection(self, direction, room):
        # TODO
        pass
        
    # Checks whether the given direction has a connection from this room.
    def has_connection(self, direction):
        # TODO
        pass

    # Retrieves room connected to this room.
    def get_connection(self, direction):
        # TODO
        pass

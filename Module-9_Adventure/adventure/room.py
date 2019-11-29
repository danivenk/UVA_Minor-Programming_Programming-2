class Room(object):

    # Initializes a Room
    def __init__(self, room_id, name, description):

        # Dictionary that maps directions like "EAST" to other room objects
        self.connections = {}

        # Room properties
        self.id = room_id
        self.name = name
        self.description = description
        self.visited = False

    # Adds a given direction and the connected room to our room object.
    def add_connection(self, direction, room):
        direction = direction.lower()
        self.connections[direction] = room
        
    # Checks whether the given direction has a connection from this room.
    def has_connection(self, direction):
        if direction in self.connections:
            return True
        else:
            return False

    # Retrieves room connected to this room.
    def get_connection(self, direction):
        return self.connections[direction]

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

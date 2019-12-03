class Room(object):

    # Initializes a Room
    def __init__(self, room_id, name, description):

        # Dictionary that maps directions like "EAST" to other room objects
        self.connections = {}
        self.items = {}

        # Room properties
        self.id = room_id
        self.name = name
        self.description = description
        self.visited = False

    # Adds a given direction and the connected room to our room object.
    def add_connection(self, direction, room, condition=""):
        direction = direction.lower()
        condition = condition.lower()

        if direction in self.connections:
            self.connections[direction][condition] = room
        else:
            self.connections[direction] = {}
            self.connections[direction][condition] = room

        
    # Checks whether the given direction has a connection from this room.
    def has_connection(self, direction):
        direction = direction.lower()
        if direction in self.connections:
            return True
        else:
            return False

    # Retrieves room connected to this room.
    def get_connection(self, direction):
        direction = direction.lower()
        return self.connections[direction]

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def add_item(self, item, item_name):
        item_name = item_name.lower()
        self.items[item_name] = item
    
    def get_items(self):
        return self.items

    def pick_up_item(self, item_name):
        item_name = item_name.lower()
        if item_name in self.items:
                return self.items.pop(item_name)
        return None


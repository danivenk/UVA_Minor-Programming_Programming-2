from room import Room

class Adventure():

    # Create rooms and items for the appropriate 'game' version.
    def __init__(self, game):

        # Rooms is a dictionary that maps a room number to the corresponding room object
        self.rooms = {}

        # Load room structures
        self.load_rooms(f"data/{game}Adv.dat")

        # Game always starts in room number 1, so we'll set it after loading
        assert 1 in self.rooms
        self.current_room = self.rooms[1]

    # Load rooms from filename in two-step process
    def load_rooms(self, filename):
        file = open(filename, "r")

        line = file.readline()

        while (line != "\n"):
            line_data = line.strip("\n").split("\t")

            self.rooms[int(line_data[0])] = Room(int(line_data[0]), line_data[1], line_data[2])

            line = file.readline()

        line = file.readline()

        while (line != "\n"):
            line_data = line.strip("\n").split("\t")

            editing_room_no = int(line_data[0])

            for data in range(1, len(line_data), 2):
                self.rooms[editing_room_no].add_connection(line_data[data], self.rooms[int(line_data[data + 1])])

            line = file.readline()

        file.close()

        for room in self.rooms:
            print(room, self.rooms[room].connections)


    # Pass along the description of the current room
    def get_description(self):
        if self.current_room.get_visited():
            return self.current_room.name
        else:
            return self.current_room.description

    # Move to a different room by changing "current" room, if possible
    def move(self, direction):
        if not self.current_room.has_connection(direction):
            return False

        if not self.current_room.get_visited():
            self.current_room.set_visited()

        move_room = self.current_room.get_connection(direction)

        self.current_room = move_room

        return True


if __name__ == "__main__":
    
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

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.get_description())

    # Prompt the user for commands until they type QUIT
    while True:

        # Prompt
        command = input("> ").lower()

        # Perform move or other command
        while (not adventure.move(command)):
            print("Invalid command")
            command = input("> ").lower()

        print(adventure.get_description())

        # Escape route
        if command == "quit":
            break

from room import Room
from item import Item

class Adventure():

    # Create rooms and items for the appropriate 'game' version.
    def __init__(self, game):

        # Rooms is a dictionary that maps a room number to the corresponding room object
        self.rooms = {}

        self.inventory = {}

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
                if "/" in line_data[data + 1]:
                    conditional_room = line_data[data + 1].split("/")
                    self.rooms[editing_room_no].add_connection(line_data[data], self.rooms[int(conditional_room[0])], conditional_room[1])
                else:
                    self.rooms[editing_room_no].add_connection(line_data[data], self.rooms[int(line_data[data + 1])])

            line = file.readline()

        line = file.readline()

        while (line != ""):
            line_data = line.strip("\n").split("\t")

            new_item = Item(line_data[0], line_data[1])

            self.rooms[int(line_data[2])].add_item(new_item, line_data[0])

            line = file.readline()

        file.close()


    # Pass along the description of the current room
    def get_description(self):
        if self.current_room.get_visited():
            return self.current_room.get_name()
        else:
            return self.current_room.get_description()

    def get_long_description(self):
        return self.current_room.get_description()

    # Move to a different room by changing "current" room, if possible
    def move(self, direction):
        if not self.current_room.has_connection(direction):
            return False

        if not self.current_room.get_visited():
            self.current_room.set_visited()

        move_room = self.current_room.get_connection(direction)

        for item in self.inventory:
            if item in move_room:
                self.current_room = move_room[item]
                return True
        self.current_room = move_room[""]

        return True

    def is_forced(self):
        if self.current_room.has_connection("forced"):
            return True
        return False

    def get_items(self):
        room_items = self.current_room.get_items()

        for item in room_items.values():
            print(item)
    
    def add_to_inventory(self, item_name):
        pickup_item = self.current_room.pick_up_item(item_name)
        if pickup_item != None:
            self.inventory[item_name] = pickup_item
            return True
        return False
    
    def del_from_inventory(self, item_name):
        if item_name in self.inventory:
            self.inventory.pop(item_name)
            return True
        return False

    def get_inventory(self):
        return self.inventory


def get_synonyms():
    with open("data/Synonyms.dat") as file:
        synonyms_dict = {}

        for line in file:
            line = line.lower().strip("\n")
            synonyms = line.split("=")

            synonyms_dict[synonyms[0]] = synonyms[1]

        return synonyms_dict


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

    synonyms = get_synonyms()

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.get_description())
    adventure.get_items()

    # Prompt the user for commands until they type QUIT
    while True:

        # Prompt
        command = input("> ").lower()

        split = False

        if " " in command:
            commands = command.split(" ")
            command = commands.pop(0)
            parameter = commands
            split = True

        if command in synonyms:
            command = synonyms[command]

        # Escape route
        if command == "quit":
            break
        elif command == "help":
            print("You can move by typing directions such as EAST/WEST/IN/OUT" + \
            "QUIT quits the game." + \
            "INVENTORY lists the item in your inventory." + \
            "LOOK lists the complete description of the room and its contents." + \
            "TAKE <item> take item from the room." + \
            "DROP <item> drop item from your inventory.")
        elif command == "look":
            print(adventure.get_long_description())
            adventure.get_items()
        elif command == "take":
            if not split:
                print("Invalid command")
                continue
            elif not adventure.add_to_inventory(parameter[0]) or len(parameter) != 1:
                print("No such item.")
                continue

            print(f"{parameter[0]} taken.")
        elif command == "drop":
            if not split:
                print("Invalid command")
                continue
            elif not adventure.del_from_inventory(parameter[0]) or len(parameter) != 1:
                print("No such item.")
                continue

            print(f"{parameter[0]} dropped.")

        elif command == "inventory":
            inventory = adventure.get_inventory()
            for item in inventory.values():
                print(item)
        else:
            if not adventure.move(command):
                print("Invalid command")
                continue

            print(adventure.get_description())
            adventure.get_items()

            while adventure.is_forced():
                adventure.move("forced")
                print(adventure.get_long_description())


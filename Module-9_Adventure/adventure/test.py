from room import *

r1 = Room(1, "Tokyo", "Capital of Japan")
r2 = Room(2, "Osaka", "2nd largest city of Japan")
r1.add_connection("West", r2)
r2.add_connection("East", r1)
rooms = {1:r1, 2:r2}
current_room = rooms[1]

move_room = current_room.get_connection("west")

print(move_room)
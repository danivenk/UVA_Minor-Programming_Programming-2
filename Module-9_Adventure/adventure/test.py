from room import *
from item import *

r1 = Room(1, "Tokyo", "Capital of Japan")
r2 = Room(2, "Osaka", "2nd largest city of Japan")
r3 = Room(2, "Kobe", "City in Hyogo")
r1.add_connection("West", r2)
r1.add_connection("West", r3, "SUICA")
r2.add_connection("East", r1)
rooms = {1:r1, 2:r2}
current_room = rooms[1]

r1.add_item(Item("SUICA", "card used to travel"), "SUICA")

for item in r1.get_items().values():
    print(item)

r1.pick_up_item("SUICA")
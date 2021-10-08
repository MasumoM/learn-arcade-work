class Room:
    """
    This is a class that represents the character of the game.
    """

    def __init__(self, description, north, east, south, west,):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# These are all the rooms of the building
def main():
    room_list = []
    # This is outside
    room = Room("You are outside of the building.", north=1, west=None, south=0, east=None)
    room_list.append(room)

    # this is room one (the lobby)
    room = Room("You are in the lobby", north=4, west=2, south=0, east=None)
    room_list.append(room)

    # This is room two (the vip room)
    room = Room("You are in the vip room", north=5, west=None, south=None, east=1)
    room_list.append(room)

    # This is room 3 (The Storage)
    room = Room("You are in the storage room", north=6, west=None, south=None, east=10)
    room_list.append(room)

    # This is room 4 (The Kitchen)
    room = Room("You are in the kitchen", north=None, west=11, south=1, east=5)
    room_list.append(room)

    # This is room 5 (The cafe)
    room = Room("You are in the cafe", north=8, west=6, south=2, east=4)
    room_list.append(room)

    # This is room 6 (The dark room)
    room = Room("You are in the dark room", north=None, west=None, south=3, east=10)
    room_list.append(room)

    # This is room 7 (The Lounge)
    room = Room("You are in the lounge", north=None, west=8, south=None, east=None)
    room_list.append(room)

    # This is room 8 (The pool room)
    room = Room("You are in the indoors pool room", north=None, west=7, south=5, east=None)
    room_list.append(room)

    # This is room 9 ( the roof top)
    room = Room("You are on the room", north=None, west=11, south=None, east=8)
    room_list.append(room)

    # This is room 10 (The west balcony)
    room = Room("You are on the German balcony", north=None, west=6, south=3, east=None)
    room_list.append(room)

    # This is room 11 (The East balcony)
    room = Room("You are on the italian balcony", north=None, west=8, south=4, east=9)
    room_list.append(room)

    current_room = 0
    print (room_list[current_room].description,"There is a passage to the north")

    done = False



























main()
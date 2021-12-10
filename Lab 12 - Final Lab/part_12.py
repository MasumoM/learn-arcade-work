class Room:

    # This is a class that represents the character of the game.

    def __init__(self, description, north, west, south, east, up, down, right,):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.right = right

# Item class, it holds all the stuff
class Item:

    def __init__(self, room_number, description, name, ):
        self.room_number = room_number
        self.description = description
        self.name = name


# These are all the rooms of the building
def main():
    room_list = []
    # This is outside
    room = Room("You are outside. There is chaos outside and people are running everywhere. "
                "\nBuildings are burning down so find an escape!", 1, None, 0, None)
    room_list.append(room)

    # this is room one (the lobby)
    room = Room("You are in the lobby. There are couches and TVs are still playing. \n"
                "There are drinks on the table and the room is very dark ", 4, 2, 0, None, None, None)
    room_list.append(room)

    # This is room two (the vip room)
    room = Room("You are in the VIP room, there is gold on the table, a gun, and a bag of cash.\n "
                "The gun only has a few bullets. The couches are comfortable but you can leave the house if you like,\n"
                "get a drink and rest, or continue to explore the house, whatever you want.", 5, None, None, 1)
    room_list.append(room)

    # This is room 3 (The Storage)
    room = Room("You are in the storage room. There are bags of food and a few dead bodies.\n "
                "The bags seem to be in good shape so you can take some if you like.", 6, None, None, 10)
    room_list.append(room)

    # This is room 4 (The Kitchen)
    room = Room("You are in the kitchen. There is something cooking on the stove.\n"
                "There is bloody knives laying on the counter so pay attention.\n"
                "There is also a sword behind the door (it may be helpful in the future).", None, 11, 1, 5)
    room_list.append(room)

    # This is room 5 (The cafe)
    room = Room("You are in the cafe. There is no one there and there is blood everywhere.\n"
                "coffee adds to your energy if you are tired. you can take a shot of coffee but be mindful.\n"
                "Don’t Drink too much!", 8, 6, 2, 4)
    room_list.append(room)

    # This is room 6 (The dark room)
    room = Room("You are in the dark room. You can't see anything\n"
                "but by going around you may find useful tools and resources.", None, None, 3, 10)
    # add navigation like north south and etc… to navigate the dark room
    # like north south and more
    room_list.append(room)

    # This is room 7 (The Lounge)
    room = Room("You are in the lounge, you can sleep and rest to regain mental intelligence.\n"
                "It will allow you to be faster than everyone else when you wake up, however \n"
                "keep in mind that things happen when you are asleep. you may get killed.\n"
                "If you feel like the risk is worth it you can sleep.", None, 8, None, None)
    room_list.append(room)

    # This is room 8 (The pool room)
    room = Room("You are in the indoors pool room. You can swim to heal your wounds.\n"
                "If the water is clean you will be fine but if dirty you get an infection.", None, 7, 5, None)
    room_list.append(room)

    # This is room 9 ( the roof top)
    room = Room("You are on the roof. you are safe here so you can now wait for the rescue helicopter.\n"
                "light up a flare to be seen by the helicopter, otherwise they will miss you.\n"
                "", None, 11, None, 8, 12, None, None)
    room_list.append(room)

    # This is room 10 (The west balcony)
    room = Room("You are on the German balcony. Find you way out of the balcony because you can get shot\n"
                "by the people outside. Find you way back inside to safety.\n"
                "If you cannot you will die", None, 6, 3, None)
    room_list.append(room)

    # This is room 11 (The East balcony)
    room = Room("You are on the Italian balcony. Great progress. Find the rooftop to get rescued.\n"
                "You do not have a lot of time to mess about, and make sure you have resources you may need\n"
                "before you go outside the building. Good luck and god speed.", None, 8, 4, 9)
    room_list.append(room)

    # This is the Hidden room 12.
    room = Room(" You are in the secret room twelve. this room has a lot of things you can take with you to escape.\n"
                "you however can only go right out of the door. \n it's not stable once you get out of the door.\n"
                "you can say in here and eat stock up all the precious stuff inside or you can leave right now with\n"
                "nothing on you.", None, None, None, None, 0, 9, 17)
    room_list.append()
    # If they pick zero they die

    current_room = 0

    done = False
    while not done:

        print()
        print(room_list[current_room].description)
        print()
        user_input = input("What do you want to do?")
        if user_input.lower() == "q" or user_input.lower() == "quit":
            print("Scream loser bye!!!!")
            break

        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("No path")
            else:
                current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("No path")
            else:
                current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("No path")
            else:
                current_room = next_room

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("No path")
            else:
                current_room = next_room

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("No path")
            else:
                current_room = next_room


main()

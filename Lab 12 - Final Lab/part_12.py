import random


class Room:

    # This is a class that represents the rooms of the game.

    def __init__(self, description, north, west, south, east):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

class Character:
    # This is a class that represents the items you find in the game which are
    # The enemies and the helpers.

    def __init__(self, room, description, health, damage, name):
        self.room = room
        self.description = description
        self.health = health
        self.name = name
        self.damage = damage
# This is the player class for the player
class Player:

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


# These are ll the rooms of the building
def main():
    print("Hello!")
    print("Welcome to roof access. the apocalypse is getting worse and the\n"
          "government have decided to burn the whole town because of the zombie overload\n"
          "most people have left but a few remain including you!")
    print("there is one chopper left in the whole town and its in the Mako hotel,"
          "\nit's up to you to find the chopper and escape with your life or possibly\n"
          "find some precious possessions of your own.")
    print()
    print("Make sure you pay close attention to everything and wish yourself some luck!")
    print("When you take some things and or leave some things they will impact you n the\n"
          "future, so be sure what you take and what you do!"
          "\n SOO, yeah. well don't stand out here get in side waiting to die,\n"
          "get inside, the door is to your north")
    print("type where you want to go and lets get going.")
    print("-------------------------------------------------------")
    # Variable

    room_list = []
    # This is outside
    room = Room("You are outside. There is chaos outside and people\n"
                "are running everywhere. "
                "\nBuildings are burning down. so find an escape!\n"
                "get inside quick", 1, None, None, None)
    room_list.append(room)

    # this is room one (the lobby)
    room = Room("You are currently in the lobby. There are couches and TVs\n"
                "are still playing.There are drinks on the table and the room\n"
                "is very dark. You can drink some bose and chill of find\n"
                "a different room. It is all up to you, as always.", None, 2, 0, None)
    room_list.append(room)

    # This is room two (the vip room)
    room = Room("You are in the VIP room, there is gold on the table, a gun,\n"
                "and a bag of cash.\nthe gun only has 2 bullets. you can take\n"
                "the pistol and continue to explore the house, whatever you want.", 5, None, None, 1)
    room_list.append(room)

    # This is room 3 (The Storage)
    room = Room("You are in the storage room. There are bags of food and a few dead bodies.\n "
                "The bags seem to be in good shape so you can take some if you like.", 6, None, None, 10)
    room_list.append(room)

    # This is room 4 (The Kitchen)
    # Take a sword, increase weight or reduce health
    room = Room("You are now in the kitchen. There is something cooking on the stove.\n"
                "There is bloody knives laying on the counter so pay attention there maybe.\n"
                "someone there who may kill you, there is also a sword behind the door\n"
                "you can take the sword(it may be helpful in the future).", None, 5, None, 11)
    room_list.append(room)

    # This is room 5 (The cafe)
    room = Room("You are in the cafe. There is no one here so do whatever you like but\n"
                "there is blood everywhere. Coffee adds to your energy if you are tired.\n"
                "you can take a shot of coffee but be mindful.\n"
                "Don’t Drink too much!", 8, 6, 2, 4)
    room_list.append(room)

    # This is room 6 (The dark room)
    room = Room("oops this room is very dark, i cant's see anything. Can you? right you cant\n"
                "You can't see anything but by going around you may find useful tools and resources.\n"
                "do you want to search the room? I would if i were you. and then you can leave after\n"
                "", None, None, 3, 10)
                # There is a health drink jar that has 2 drinks if they are all drunk
                # fast the character passes out and probably dies.

    # add navigation like north south and etc… to navigate the dark room
    # like north south and more
    room_list.append(room)

    # This is room 7 (The Lounge)
    room = Room("You are in the lounge, you can sleep and rest to regain mental intelligence.\n"
                "It will allow you to be faster than everyone else when you wake up, however \n"
                "keep in mind that things happen when you are asleep. you may get killed.\n"
                "If you feel like the risk is worth it you can """"sleep"""".", None, None, None, 8)
    room_list.append(room)

    # This is room 8 (The pool room)
    room = Room("whew.. that was something at least you are still alive.You are in the indoors\n"
                "pool room. You can /swim/ to heal your wounds.If the water is clean you will be fine\n"
                "but if dirty you get an infection.it's the way it is", None, 7, 5, 9)
    room_list.append(room)

    # This is room 9 ( the roof top)
    room = Room("You are on the roof access room. you are safe here so you can now climb north to.\n"
                "the roof access, otherwise you may be caught and killed.\n"
                "", 12, 8, None, 11)
    room_list.append(room)

    # This is room 10 (The west balcony)
    room = Room("You are on the German balcony now, HORRIBLE VIEW. Find you way out of the\n"
                "balcony because you can get shot by the people outside. Find you way back\n"
                "inside to safety.If you cannot you will die", 6, 7, 3, 6)
    room_list.append(room)

    # This is room 11 (The East balcony)
    room = Room("You are on the Italian balcony. Great progress. Find the rooftop to get rescued.\n"
                "You do not have a lot of time to mess about, and make sure you have resources you may need\n"
                "before you go outside the building. Good luck and god speed.", 9, None, 4, 15)
    room_list.append(room)

    # This is the Hidden room 12. room on roof
    # If they pick zero they die
    room = Room("You are in the secret room twelve. this room has a lot of things you can take with you to escape.\n"
                "you however can only go west out of the door. the access back in the building is gone\n"
                "it's not stable once you get out of the door.You can say in here and eat or stock up all the\n"
                "precious stuff inside or you can leave right now with nothing on you.", None, 13, 9, None)
    room_list.append(room)

    # This is the room 13
    # It only goes to the end room 14 is the end
    room = Room("you are on the helipad, you have done a great job.\n"
                "now! you don't happen to have a gallon of gas on you /n"
                "for this chopper. anyway lets get out of here", 14, None, 7, None)
    room_list.append(room)

    # 15
    # Jumping off the balcony/ you're dead
    room = Room("You jumped of the balcony", None, None, None, None)
    room_list.append(room)

    current_room = 0

    # This is where every room's choices are built
    choice_list = []

    # Room 1
    choice = Character(1, "Have some drink", 50, 15, "drink")
    choice_list.append(choice)

    # Room 2
    # This is the gold
    choice = Character(2, "The Gold?", 50,
                       15, "gold")
    choice_list.append(choice)

    # Room 3
    # This is the food
    choice = Character(3, "Oh yeah, that's some food.... "
                      "\nif you want to heat it will add to your energy.", 20,
                      None, "food",)
    choice_list.append(choice)

    # This is the bodies
    choice = Character(3, "looks like there is some bodies, ergh nasty"
                          "\nif you want to inspect them, you can, but be careful.", 20,
                       80, "bodies")
    choice_list.append(choice)

    # Room 4
    # This is the sword
    choice = Character(4, "we found a sword"
                          "\nif you want extra protection you can take it.", 50,
                       None, "sword", )
    choice_list.append(choice)

    # Room 5
    # If you drink again it will reduce your health
    choice = Character(5, "Heck yes, we got some coffee, energy will be up i the shot stopper\n"
                      "\nget it? shot stoper?.......Nevermind"
                      "\nit will boost your energy. But too-much is not good.", 40, 10, "coffee",)
    choice_list.append(choice)

    # Room 6
    # If you sleep it's a risk
    choice = Character(6, "Well this is an empty one... Well, move on", None, None, "empty room")
    choice_list.append(choice)

    # Room 7
    # if they sleep all their stuff disappear and health reduced
    choice = Character(7, "Well this is a nice bedroom. You can rest on the\n"
                          "\ncomfy bed......."
                          "\nit will boost your energy. if you sleep you're in danger.", 40, 20, "rest", )
    choice_list.append(choice)

    # Room 8
    # This is a roof access
    choice = Character(8, "We got ourselves a swimming pool, you can swim to heal yourself\n"
                          "be mindful that it's a risk,", 100, 20, "swim")
    choice_list.append(choice)

    # Room 9
    choice = Character(9, "Yes, we got a staircase which will access the top if i'm right\n"
                          "we are almost there. Good work. I would access roof if i were you\n"
                          , None, None, "access roof")
    choice_list.append(choice)

    # Room 10
    choice = Character(10, "Just a balcony nothing special. Move on", None, None, "balcony")
    choice_list.append(choice)

    # Room 11
    choice = Character(11, "Just a balcony nothing special. Move on", None, None, "balcony")
    choice_list.append(choice)

    # This is the gas
    choice = Character(12, "The gas can maybe. you can take the gas can", 50, None, "gas")
    choice_list.append(choice)

    # Room Number 13
    choice = Character(13, "i would 'fly away' if i were you\n"
                         , 100, None, "fly away")
    choice_list.append(choice)

    player = Player(70, 15)

    # User input stuff
    done = False
    room_change = True
    while not done:
        if room_change:

            # User choice
            # Talks about the room
            print(room_list[current_room].description)

            # Going into the room triggers the items in the room
            for choice in choice_list:
                if choice.room == current_room:
                    print(room.description and choice.description)
            room_change = False
        user_choice = input("\nWant do you want to do?  ")
        print()
        # User options

        # If user quits
        if user_choice.lower() == "quit":
            print("Scream loser bye!!!! I hope you DIE")
            done = True

        # If user wants to go north
        elif user_choice.lower() == "north":
            next_room = room_list[current_room].north
            room_change = True
            if next_room is None:
                print()
                print("\nYou can't go there. find another way to the next room")
            else:
                current_room = next_room

        # If user wants to go east
        elif user_choice.lower() == "east":
            next_room = room_list[current_room].east
            room_change = True
            if next_room is None:
                print()
                print("\n It looks like you cannot go in that direction. Go another way")
            else:
                current_room = next_room

        # If user wants to go south
        elif user_choice.lower() == "south":
            next_room = room_list[current_room].south
            room_change = True
            if next_room is None:
                print()
                print("It looks like you cannot go in that direction. Find another way")
                print()
            else:
                current_room = next_room

        # If user wants to go west
        elif user_choice.lower() == "west":
            next_room = room_list[current_room].west
            room_change = True
            if next_room is None:
                print()
                print("\nNope you cannot migrate to the cali coast. Sorry not sorry.\n"
                      "any who, let's move on.")
            else:
                current_room = next_room

        # The user chose to drink
        elif user_choice.lower() == "drink":
            print()
            print("\nAlright! let's drink! I am sure you are not underage at all?"
                  "\ndon't drink too much though because you will be drunk. There is"
                  "\nnothing worse than trying to escape drunk!")
            print()
            print("Anyway, what do you want? beer or beer? haha")

        # The user then has to pick what to drink.
        # If Beer
        if user_choice.lower() == "beer":
            for choice in choice_list:
                if choice.room == current_room:
                    player.damage = random.randrange(1, 30)
                    choice.health -= player.damage
                    print()
                    print("Oh yeah! oh yeah that's some good beer!")
                    print("That beer took", choice.health, " from us\n"
                                                                        "WHOOPS")
                    if choice.damage == 30:
                        print()
                        print("Well I told you not to drink")
                        player.health = 70
                    else:
                        print("You're going to be weak now, at least for a while")
                        player.health = player.health - choice.damage

        #If player chose coffee
        if user_choice.lower() == "coffee":
            for choice in choice_list:
                if choice.room == current_room:
                    player.health = random.randrange(1, 30)
                    choice.health += player.damage
                    print()
                    print("Oh yeah! oh yeah that's some good caffeine baby!")
                    print("That added", choice.health, "to our health, that's what i'm talking about\n"
                                                                        "Yeah!!")
                    if choice.damage == 30:
                        print()
                        print("Coffee always works")
                        player.health = 70
                    else:
                        print("Now that we have more energy, lets continue")
                        player.health = player.health - choice.damage

        # If player chose gas or get gas
        elif user_choice.lower() == "gas" or user_choice.lower() == "get gas":
            for choice in choice_list:
                if choice.room == current_room:
                    player.health = random.randrange(1, 30)
                    choice.health += player.damage
                    print()
                    print("That's a great idea just in case you need it")

                    if choice.damage == 30:
                        print()
                        print("Coffee always works")
                        player.health = 70
                    else:
                        print("Now that we have gas, we can use it if we need to")
                        player.health = player.health

        # If player chose swim
        if user_choice.lower() == "swim":
            for choice in choice_list:
                if choice.room == current_room:
                    player.health = random.randrange(1, 30)
                    choice.health += player.damage
                    print()
                    print("Wow, I am surprised with how clean that water is")
                    print("That added", choice.health, "to our health, that's great and refreshing\n"
                                                               "Yeah!!")
                    if choice.damage == 30:
                        print()
                        print("Coffee always works")
                        player.health = 70
                    else:
                        print("Now we can find the roof and get out of this place, lets continue")
                        player.health = player.health - choice.damage

        # If player chose fly away
        elif user_choice.lower() == "fly away":
            for choice in choice_list:
                if choice.room == current_room:
                    player.health = player.health
                    choice.health += player.damage
                    print()

                if choice.damage == 30:
                    print()
                    print("Never see you again losers")
                    player.health = 70
                else:
                    done = True
                    print("You are safe now")
                    print("YOU WON")

        # If player chose eat
        if user_choice.lower() == "eat":
            for choice in choice_list:
                if choice.room == current_room:
                    player.health = random.randrange(1, 30)
                    choice.health += player.damage
                    print()
                    print("Oh yeah! that's tasty ")
                    print("That added", choice.health, "to our health, that's what i'm talking about\n"
                                                               "Yeah!!")
                    if choice.damage == 20:
                        print()
                        print("definitely italian")
                        player.health = 70
                    else:
                        print("Now that we have more energy, lets continue")
                        player.health = player.health

        # If player choose gold
        elif user_choice.lower() == "gold":
            for choice in choice_list:
                if choice.room == current_room:
                    player.damage = random.randrange(1, 30)
                    choice.health += player.damage
                    print()
                    print("Well the gold is heavy so we're gonna weight a bit!")
                    print("The gold will make is lose", choice.health, " of health\n"
                                                           "but it's worth it. I hope")
                    if choice.damage == 30:
                        print()
                        print("That's heavy")
                        player.health = 100
                    else:
                        print()
                        player.health = player.health - choice.damage

        # If player choose cash
        elif user_choice.lower() == "cash":
            for choice in choice_list:
                if choice.room == current_room:
                    player.damage = random.randrange(1, 30)
                    choice.health += player.damage
                    print()
                    print("Money never hurt")
                    print("we will have to come with loss of", choice.health, "of health\n"
                                                                               "but it's worth it. you can buy a gym after")
                    if choice.damage == 30:
                        print()
                        print("That's heavy")
                        player.health = 80
                    else:
                        print()
                        player.health = player.health - choice.damage

        # If they pick gun.
        elif user_choice.lower() == "gun":
            for choice in choice_list:
                if choice.room == current_room:
                    player.damage = random.randrange(1, 30)
                    choice.health -= player.damage
                    print("Oh yeah! oh yeah, that's a gun!")
                    print("That gun took", choice.health, " from us\n")
                    if choice.damage == 30:
                        print("It will be worth it whe there is an enemy")
                    else:
                        player.health = player.health

        if user_choice.lower() == "check health":
            print()
            if player.health <= 10:
                print("You're low on health! Be super careful! death is real you know")
                print("Health:", player.health)

            elif player.health <= 50:
                print("Well, we are still alive! It's just a small wound!")
                print("Health:", player.health)

            else:
                print("Don't check the health. You are barely drunk!")
                print("Health:", player.health)




# Main function
main()
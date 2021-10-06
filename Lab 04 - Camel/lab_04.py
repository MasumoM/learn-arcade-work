# Lab 04: Camel game Assignment(Fighter Fight)

import random

# Introduction to the game
print("Welcome to RUSH")
print("You have stolen a top secret fighter jet from the Russian Air force you are making you way to the US ship.")
print("The Russian fighters are chasing you, they want to shut you down!")
print("Outrun the Russian fighter pilots and survive the rush")
print()

# The start of the game controls
done = False
milesTraveled = 0
russiansTraveled = -20
engine_heat = 0
g_force_sickness = 0
fuel_left = 3
radarJam = -1
# The loop of the Game
while not done:

    # Options the player has
    print("A. reduce G- Force to rest.")
    print("B. Continue full speed.")
    print("C. Continue moderate speed.")
    print("D. Radar Jam.")
    print("E. Status check.")
    print("Q. Quit.")
    print()

    # Take in Gamers input
    userInput = input("What is your decision Capitan? ")

    # Check if the user wants to quit
    if userInput.upper() == "Q":
        done = True
        print("Exiting Game. Say hallo to heaven!")

    elif userInput.upper() == "B" * 3:
        engine_heat = 50
        fuel_left = 0
        g_force_sickness = 50
        done = True

    # Status update
    elif userInput.upper() == "E":
        print("Miles traveled:", milesTraveled)
        print("Fuel Left:", fuel_left)
        print("The Russians are", milesTraveled - russiansTraveled, "miles behind you.")
        print()
        print("Make a choice")
        print()

    # (Radar Jam) which is the same as resting
    elif userInput.upper() == "D":
        print("You Jam their Radar tracker.")
        print("They have lost your trail, you are safe to continue")
        print("The Russians don't stop, they are still hunting.")
        print()
        print("What are you to do?")
        print()
        g_force_sickness = 0
        russiansTraveled += random.randrange(7, 15)

    # Continuing Moderate speed!!!
    elif userInput.upper() == "C":
        milesTraveled = random.randrange(8, 17)
        milesTraveled += milesTraveled
        g_force_sickness -= 1
        engine_heat -= 1
        russiansTraveled += random.randrange(2, 5)
        radarJam = random.randrange(20)
        if radarJam == 10:
            print("Radar Jam range coming up")
            g_force_sickness = 0
            engine_heat = 0
            fuel_left = 8
            print("As you continue to escape the radar jam becomes available!")
            print("you Jam their Radar and rest")
            print("The engine is cooled down")
            print("The Russians are still chasing they will shoot when in range")
            print()
        else:
            print("You Continue forward, moving a total of", milesTraveled, "miles")
            print("Your tiredness increases.")
            print("The Russians do not quit.")
            print()
    # Continuing Full speed
    elif userInput.upper() == "B":
        miles = random.randrange(10, 21)
        milesTraveled += miles
        g_force_sickness += 1
        fuel_left += random.randrange(0, 5)
        russiansTraveled += random.randrange(7, 15)
        radarJam = random.randrange(20)
        if radarJam == 10:
            g_force_sickness = 0
            engine_heat = 0
            fuel_left = 3
            print("As you are out of their range!")
            print("you cool down the engine to save gas, you recover your body and also")
            print("The engine is in the green range")
            print("The Russians are not giving up!")
            print()

        if milesTraveled >= 200:
            print("Welcome to USS Ferrari captain great flying, you lost the Russians")
            print("YOU WIN!!!")
            print()
            done = True

        else:
            print("You Push ahead full speed hopping to reach the Ship, moving a total of", milesTraveled, "miles")
            print("Your sickness is increasing.")
            print()
            print("The Russians continue to chase you.")
            print()
    # Reduce G- force to survive
    elif userInput.upper() == "A":
        if fuel_left > 0:
            fuel_left += 1
            g_force_sickness = 1
            print("You reduce the Gs")
            print("you are able to rest your body and cool dow the engine")
            print("however the Russian pilots are still chasing you")
            print("If you don't do something about it you will get caught!!")
            print()
        else:
            print("Your g force tolerance is very low, you can see yourself dying")
            print()

    # This is status check code
    # G force sickness and tolerance
    if g_force_sickness > 8:
        print("You passed out and crashed the Jet! Straight out of the sky")
        print("Game Over.")
        print()

        done = True
    elif g_force_sickness > 4:
        print("G force tolerance is low")

    # Check for the distance the player traveled and progress to win

    if milesTraveled >= 1000:
        print("Welcome to USS Ferrari captain great flying, you lost the Russians")
        print("YOU WIN!!!")
        print()
        done = True

# Engine Heat and  the life of the Jet
    if engine_heat >= 8:
        print("Your Engine exploded from overheating!!!")
        print("With no Jet You ejected and froze to death!!")
        print("After only four minutes outside the jet")
        print("GAME OVER !!!")
        print()
        done = True

    elif engine_heat >= 5:
        print("Your engine is overheating")
        print("return the engine to the green zone to make sure it doesn't explode")
        print()

    elif fuel_left >= 2:
        print("You are running out of fuel")

    elif fuel_left >= 0:
        print("You ran out of fuel")
        done = True

    # The Russians distance from your Jet
    if milesTraveled - russiansTraveled <= 1:
        print("The Russians have caught your Jet / well their Jet")
        print("They shoot you down and return back to base. oops!")
        print()
        print("GAME OVER!!!.")
        print()
        done = True

    elif milesTraveled - russiansTraveled < 10:
        print("You see Russian aircraft getting closer on the Radar.")
        print("The Russians are getting very very close close!!")
        print()
    # The end of the Game (End of the Game message)
input()

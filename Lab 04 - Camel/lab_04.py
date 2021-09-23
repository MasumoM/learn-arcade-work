import random

for i in range(20):
    my_number = random.randrange(1, 6)
    print(my_number)

for i in range(5):
    my_number = random.randrange(5)
    if my_number == 0:
        print("Dragon")
    else:
        print("No Dragon")

my_number = random.randrange(5)
if my_number == 0:
    print("Dragon")
else:
    print("No Dragon")


# You get a random floating point
my_number = random.random()
print("my_number * 9 - 1")

# Quick review:

# Write a function called count_up that takes in two numbers.
# prints all the numbers from the start to finish inclusive.
# Test with 5, 10

def count_up(start, end):
    for number in range(start, end + 1):
        print(number)

count_up(5, 10)
# This worked and counted 5 6 7 8 9 10

quit = "n"
while quit.lower() == "n" or quit.lower() == "no":
    quit = input("Do you want to quit? ")

done = False

while done = False:
    quit = input("Do you want to quit? ")
    if quit.lower() == "y":
        done = True
        print("Bye!")
        break


    attack = input("Do you want to attack the dragon? ")
    if attack.lower() == "y":
        done = True
        print("Bad choice, you died!")

import random





















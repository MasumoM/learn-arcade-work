x = 3
print("x =", x, "and is of type:", type(x))

x = 3.241
print("x =", x, "and is of type:", type(x))

x = "Hi there"
print("x =", x, "and is of type:", type(x))

x = True
print("x =", x, "and is of type:", type(x))

x = 3
print(x)
x = 4
print(x)

# Also can do this

# Defaults to tuple if you don't include parenthesis
x = (2, 3, 4, 5)
print("x =", x, "and is of type:", type(x))

x = (2, 3, 4, 5)
print("x =", x, "and is of type:", type(x))
x = [2, 3, 4, 5]
print("x =", x, "and is of type:", type(x))


# New and important stuff
x = [10, 20]
print(x[0])

# Another common mistake
x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x[1])
# This will work because it involves the list and the position
# starts with zero which is in position 3 and 8 is in position 1

# Use an negative one to get the end of the list
x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x[-1])


x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x[1])

# this will replace the number in position 2 with 22
x[2] = 22
print(x)

# This will not work
x = 18
print(x)

# You can make a list with nothing in it (empty list)
x = []
print(x)

# (Len) function prints the number of elements in a list

# You can even print words and other lists within the lists
my_list = ["knife", "spoon", "fork"]
my_list = [[4, 6], [2, 10]]

for item in my_list:
    print(item)

my_list = [2, 3, 6, 5, 8, 10, 31]

for i in range(len(my_list)):
    print(item)

for i in range(len(my_list)):
    print("Item", i, "is", my_list[i])

# Tis is the better way of doing 74 and 69 use this instead
for index, value in enumerate(my_list):
    print("Item", index, "is", value)

# A method
my_list = [2, 3, 6, 5, 8, 10, 31]
print(my_list)
my_list.append(100)
print(my_list)



# This is an example of a list from scratch
my_list = []

for i in range(5):
    user_input = int(input("Enter an integer: "))
    my_list.append(user_input)

print(my_list)


my_list = ["surprise"] * 100
print(my_list)


# The sum or subtract of a list example
my_list = [2, 3, 6, 5, 8, 10, 60, 37, 31]

list_total = 0

for i in my_list:
    list_total += item

print(list_total)

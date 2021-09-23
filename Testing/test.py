temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")


# " 'for loops' - when you know how many times to loop
# 'while' - until a condition

for star_count in range(10, -1, -1):
    print(star_count )


print("the second test")
for item in [2, 6, 4, 2, 4, 6, 7, 4]:
    print(item)

print("The third test")
# What does this print? Why?
for i in range(12):
    print("a")
for j in range(12):
    print("b")

# Lab 4
for hour in range(1, 13):
    for minute in range(60):
        print(hour, minute)

total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    total = total + new_number
print("The total is: ", total)

for i in range(5):
    print("Hello")

print("there")

for i in range(5):
    print("Hello")

print("there")

a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)

# For loops
for i in range(10):
    print(i)
# You only use range in 'For Loops'
i = 0
while i < 10:
    print(i)
    i += 1

# While loop that starts with ten and end at zero
i = 1
while i >= 0:
    print(i)
    i -= 1

plain_text = "This is a test. ABC abc"

# Julious Ceasor code and secret codes
for c in plain_text:
    x = ord(c)
    x += 1
# Chr takes numbers and turn into a letter
    c2 = chr(x)
# Ord is the ordinal value, it takes letter and turn it into a number
    print(c2, end=" ")


my_list = [4, 2, 56, 2, 0]

biggest_number = my_list[0]
for item in my_list:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))

month = months[(n - 1) * 3:(n - 1) * 3 + 3]
print(month)

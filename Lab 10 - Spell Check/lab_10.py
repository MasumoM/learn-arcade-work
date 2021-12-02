import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


key = "Morgiana the Shrew"
current_list_position = 0

while current_list_position < len(AliceInWonderLand200.txt) and name_list[current_list_position] != key:

    # Advance to the next item in the list
    current_list_position += 1

if current_list_position < len(name_list):
    print("The name is at position", current_list_position)
else:
    print("The name was not in the list.")


key = "Morgiana the Shrew"
lower_bound = 0
upper_bound = len(name_list)-1
found = False

# Loop until we find the item, or our upper/lower bounds meet
while lower_bound <= upper_bound and not found:

    # Find the middle position
    middle_pos = (lower_bound + upper_bound) // 2

    # Figure out if we:
    # move up the lower bound, or
    # move down the upper bound, or
    # we found what we are looking for
    if name_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif name_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print( "The name is at position", middle_pos)
else:
    print( "The name was not in the list." )
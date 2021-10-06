import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

# Explore this

#1: Pyramid from 10 - 54
print("Number 1: Pyramid")
n = 10
for row in range (10):
    for column in range(row):
        print (n, end=" ")
        n += 1
    print()
print()
#2: Print a Box of N Size
print("Number 2: Print a Box of N Size")
n = input("How big do you want your box (enter a digit)?")
n = int(n)
for top in range (1):
  for column in range (n*2):
    print("o", end="")
print()

for middle in range(n*2-2):
  for j in range (1):
    print("o", end="")
  for j in range (n*2-2):
    print(" ", end="")
  for j in range (1):
    print("o", end="")
  print()

for bottom in range (1):
  for column in range (n*2):
    print("o", end="")

#To here






def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    pass


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    pass


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    pass


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    pass


def draw_section_6():
    pass


def draw_section_7():
    pass


def draw_section_8():
    pass


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()

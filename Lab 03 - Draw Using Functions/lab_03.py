import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# This opens the window to start drawing
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    # The Sun
    arcade.draw_circle_filled(300, 200, 110, arcade.color.ORANGE)

    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

    # This is a drawing of the birds on the top left of the screen
    arcade.draw_arc_outline(center_x=90,
                            center_y=440,
                            width=35,
                            height=36,
                            color=arcade.csscolor.BLACK,
                            start_angle=0,
                            end_angle=90,
                            border_width=6,
                            tilt_angle=45)

    arcade.draw_arc_outline(center_x=135,
                            center_y=440,
                            width=35,
                            height=36,
                            color=arcade.csscolor.BLACK,
                            start_angle=0,
                            end_angle=100,
                            border_width=6,
                            tilt_angle=45)

    arcade.draw_arc_outline(center_x=155,
                            center_y=480,
                            width=35,
                            height=36,
                            color=arcade.csscolor.BLACK,
                            start_angle=0,
                            end_angle=100,
                            border_width=6,
                            tilt_angle=45)

    arcade.draw_arc_outline(center_x=90,
                            center_y=480,
                            width=35,
                            height=36,
                            color=arcade.csscolor.BLACK,
                            start_angle=0,
                            end_angle=100,
                            border_width=6,
                            tilt_angle=45)

    arcade.draw_arc_outline(center_x=45,
                            center_y=465,
                            width=35,
                            height=36,
                            color=arcade.csscolor.BLACK,
                            start_angle=0,
                            end_angle=100,
                            border_width=6,
                            tilt_angle=45)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
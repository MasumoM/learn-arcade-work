import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# This opens the window to start drawing

    # The Sun
def draw_sun():
    # Sun
    arcade.draw_circle_filled(300, 200, 110, arcade.color.ORANGE)

    # Draw the ground
def draw_lake():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_birds():
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

def draw_clouds(x, y):
    # The Left Cloud
    arcade.draw_circle_filled(500 + x, 497 + y, 20, arcade.color.WHITE,)

def draw_cloud(x, y):
    # Middle Cloud
    arcade.draw_circle_filled(575 + x, 500 + y, 25, arcade.color.WHITE, num_segments=32)

def draw_small_cloud(x, y):
    arcade.draw_circle_filled(500 + x, 497 + y, 10, arcade.color.WHITE, num_segments=32)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_sun()
    draw_lake()
    draw_birds()
    draw_clouds(50, 0)
    draw_cloud(5, 0)
    draw_small_cloud(110,0)

    draw_clouds(-60, 70)
    draw_cloud(-160, 70)
    draw_small_cloud(-35, 70)

    draw_clouds(20, 70)
    draw_cloud(-30, 70)
    draw_small_cloud(69, 70)

    draw_clouds(200, 50)
    draw_cloud(150, 50)
    draw_small_cloud(-35, 40)
    draw_small_cloud(35, 45)
    draw_small_cloud(230, 30)

        # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
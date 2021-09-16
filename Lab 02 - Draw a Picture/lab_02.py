import arcade

# Open a window
arcade.open_window(575, 570, "Drawing of an Incomplete and sleeping mickey Mouse head")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
# Ready to draw
arcade.start_render()

# The Ears
arcade.draw_circle_filled(190, 230, 70, (18, 17, 17))
arcade.draw_circle_filled(180, 440, 70, (18, 17, 17))

arcade.draw_circle_filled(190, 230, 60, (0, 0, 0))
arcade.draw_circle_filled(180, 440, 60, (0, 0, 0))
# The Face
arcade.draw_circle_filled(350, 350, 150, (115, 17, 18))
arcade.draw_circle_filled(350, 350, 140, (105, 15, 15))

# The red details in the ear
arcade.draw_arc_outline(center_x=180,
                        center_y=440,
                        width=60,
                        height=100,
                        color=arcade.csscolor.DARK_RED,
                        start_angle=0,
                        end_angle=180,
                        border_width=6,
                        tilt_angle=45)
arcade.draw_arc_outline(center_x=190,
                        center_y=240,
                        width=60,
                        height=100,
                        color=arcade.csscolor.DARK_RED,
                        start_angle=0,
                        end_angle=180,
                        border_width=6,
                        tilt_angle=-235)
# The eyes
arcade.draw_ellipse_filled(395, 290, 90, 60, arcade.csscolor.WHITE_SMOKE)
arcade.draw_ellipse_filled(400, 400, 90, 60, arcade.csscolor.WHITE_SMOKE)

# The offset smile
arcade.draw_line(500, 220, 550, 400, (0, 0, 0), 10)

# The neck
arcade.draw_rectangle_filled(348, 173, 45, 60, arcade.color.BLACK)

# The Arms
arcade.draw_ellipse_filled(348, -70, 330, 500, arcade.color.BLACK)
arcade.draw_arc_filled(348, -70, 330, 500, (16, 94, 92), 0, 180)
arcade.draw_ellipse_filled(348, -70, 200, 400, arcade.csscolor.SKY_BLUE)
# The body
arcade.draw_ellipse_filled(348, -110, 140, 500, arcade.color.BLACK)
arcade.draw_rectangle_filled(350, 97, 120, 115, (16, 94, 92))
# The Belly Button
arcade.draw_circle_filled(348, 10, 5, arcade.csscolor.WHITE_SMOKE, num_segments=32)
# Finish drawing
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()

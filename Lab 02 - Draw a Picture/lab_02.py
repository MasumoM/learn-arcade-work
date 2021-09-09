
import arcade

# Open a window
arcade.open_window(900, 800, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
#Ready to draw
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 900, 220, 0, arcade.color.BITTER_LIME)
arcade.draw_lrtb_rectangle_filled(0, 900, 220, 0, (88, 161, 21))
arcade.draw_line(0, 60, 800, -5, arcade.color.WHITE )























# Finish drawing
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()
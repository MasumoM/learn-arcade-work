"""
This is lab 2 which i need to draw an image using Python code. Here we go.
"""

# import the arcade "arcade" library
import arcade

#opening a window to work on
arcade.open_window(800, 600, "Drawing perimeters")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

#ready to start drawing. this will be fun
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.LIGHT_GREEN)

























# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
import random
import arcade

SPRITE_SCALING = 0.4
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_PLAYER = .1
SPRITE_SCALING_BLOCK = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Atack"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7
PLAYER_SIZE = 0.4
collectcoin_sound = arcade.load_sound("sound.wav")


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.score = 0
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("tenor_3.gif",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 160
        self.player_sprite.center_y = -100
        self.player_list.append(self.player_sprite)

        #coins
        coordinate_list = [[110, 30],
                           [110, -10],
                           [110, -80],
                           [110, -170],
                           [110, -250],
                           [470, 50],
                           [470, 100],
                           [470, 150],
                           [470, 200],
                           [470,250],
                           [690,250],
                           [750, 250],
                           [800, 250],
                           [850, 250],
                           [900, 250],
                           [800, -250],
                           [800, -300],
                           [800, -200],
                           [800, -350],
                          [800, -150],
                           [800, -100],
                           [800, -50],
                           [150, -340],
                           [200, -340],
                           [250, -340],
                           [310, -340],
                           [370, -340],
                           [420, -340],
                           [490, -340],
                           [560, -430]]


        for coordinate in coordinate_list:
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
            coin.center_x = coordinate[0]
            coin.center_y = coordinate[1]
            self.coin_list.append(coin)

        # Create a row of boxes

        for x in range(13, 1240, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = -400
            self.wall_list.append(wall)

        for x in range(13, 1240, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 315
            self.wall_list.append(wall)

        for x in range(16, 220, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        for x in range(11, 250, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = x +600
            wall.center_y = 90
            self.wall_list.append(wall)
        # Create a column of boxes

        #ACTORS
        for y in range(-400, 368, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 12
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(-400, 364, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 1290
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(-290, 80, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 200
            wall.center_y = y + 10
            self.wall_list.append(wall)

        for y in range(-309, 34, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 400
            wall.center_y = y + 100
            self.wall_list.append(wall)

        for y in range(-360, 34, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 700
            wall.center_y = y + 30
            self.wall_list.append(wall)

        for y in range(-160, 34, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 1000
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(-160, 34, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 560
            wall.center_y = y -50
            self.wall_list.append(wall)

        for y in range(-160, 34, 64):
            wall = arcade.Sprite("tenor_3.gif",
                                 SPRITE_SCALING_BLOCK)
            wall.center_x = 850
            wall.center_y = y -120
            self.wall_list.append(wall)

        for y in range(-160, 34, 64):
            wall = arcade.Sprite("tenor_3.gif",
                                 SPRITE_SCALING_BLOCK)
            wall.center_x = 1050
            wall.center_y = y -170
            self.wall_list.append(wall)

        for y in range(-160, 34, 64):
            wall = arcade.Sprite("boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 1190
            wall.center_y = y +210
            self.wall_list.append(wall)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Select the camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time, hit_list=None):
        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


        # Scroll the screen to the player
        self.scroll_to_player()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(collectcoin_sound)

    def scroll_to_player(self):

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
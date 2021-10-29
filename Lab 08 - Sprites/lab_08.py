import random
import arcade

SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.020
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("monkey.png", SPRITE_SCALING_PLAYER)
        # monkey image form BrainPOP: https://www.brainpop.com/science/diversityoflife/primates/
        self.player_sprite.center_x = 20
        self.player_sprite.center_y = 20
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            coin = arcade.Sprite("banana_3.png", SPRITE_SCALING_COIN)
            # banana image from "KissClip art": https://www.kissclipart.com/banana-clipart-banana-animation-awporm/
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.coin_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        if key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()




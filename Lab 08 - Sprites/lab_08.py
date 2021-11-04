import random
import arcade

SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.1
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, )

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

            coin = arcade.Sprite("banana_7.gif", SPRITE_SCALING_COIN)
            # banana image from "KissClip art": https://www.kissclipart.com/banana-clipart-banana-animation-awporm/
            # image from "pngwing":https://www.pngwing.com/en/search?q=banana+Gif
            # image from "giphy": https://giphy.com/stickers/yellow-smoothie-banana-Ifyl6EMTA1E48HopRt
            # image "rotten banana 8 from "anatunez": https://www.anatunez.com/logos
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)


    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        if len(self.coin_list) == 0:
            arcade.draw_text("GAME OVER", 50, 50, arcade.color.WHITE, 80)

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

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()




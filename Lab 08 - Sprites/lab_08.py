import random
import arcade
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.1
BANANA_COUNT = 50
ROTTEN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Banana(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 50,
                                         SCREEN_HEIGHT + 100)

        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1.5

        if self.top < 0:
            self.reset_pos()


class Rotten(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Moving the banana
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x += -1

        if self.right > SCREEN_WIDTH:
            self.change_x += -1

        if self.bottom < 0:
            self.change_y += -1

        if self.top > SCREEN_HEIGHT:
            self.change_y += -1


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, )

        # Variables that will hold sprite lists
        self.player_list = None
        self.banana_list = None
        self.rotten_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.GRAPE)

        self.banana_sound = arcade.load_sound("banana.wav")
        self.rotten_sound = arcade.load_sound("rotten.wav")
        # sounds from Python Arcade Library:https://api.arcade.academy/en/latest/resources.html

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.banana_list = arcade.SpriteList()
        self.rotten_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("monkey.png", SPRITE_SCALING_PLAYER)
        # monkey image form BrainPOP: https://www.brainpop.com/science/diversityoflife/primates/
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(BANANA_COUNT):

            banana = Banana("banana_7.gif", SPRITE_SCALING_COIN)

            banana.center_x = random.randrange(SCREEN_WIDTH)
            banana.center_y = random.randrange(SCREEN_HEIGHT)
            banana.change_x = random.randrange(-5, 6)
            banana.change_y = random.randrange(-5, 6)

            # Add the coin to the lists
            self.banana_list.append(banana)

        for i in range(BANANA_COUNT):
            rotten = Rotten("rotten_banana_8.gif", SPRITE_SCALING_COIN)

            rotten.center_x = random.randrange(SCREEN_WIDTH)
            rotten.center_y = random.randrange(SCREEN_HEIGHT)
            rotten.change_x = random.randrange(-3, 4)
            rotten.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.rotten_list.append(rotten)

    def on_draw(self):
        arcade.start_render()
        self.banana_list.draw()
        self.player_list.draw()
        self.rotten_list.draw()

        if len(self.banana_list) == 0:
            arcade.draw_text("GAME OVER", 50, 50, arcade.color.WHITE, 80)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.banana_list) > 0:

            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        if len(self.banana_list) > 0:
            if len(self.rotten_list) >= 25:
                self.banana_list.update()
                self.rotten_list.update()

                hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.banana_list)

                for banana in hit_list:
                    banana.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.banana_sound)

                hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.rotten_list)

                for rotten in hit_list:
                    rotten.remove_from_sprite_lists()
                    self.score -= 1
                    arcade.play_sound(self.rotten_sound)
                    # banana image from "KissClip art": https://www.kissclipart.com/banana-clipart-banana-animation-awporm/
                    # image from "pngwing":https://www.pngwing.com/en/search?q=banana+Gif
                    # image from "giphy": https://giphy.com/stickers/yellow-smoothie-banana-Ifyl6EMTA1E48HopRt
                    # image "rotten banana 8 from "anatunez": https://www.anatunez.com/logos


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()




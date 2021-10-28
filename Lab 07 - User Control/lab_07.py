import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    class MyApplication(arcade.Window):

        def __init__(self, width, height):
            super().__init__(width, height, "Trigger Sound With Key")

            # Load the sound when the application starts
            self.laser_sound = arcade.load_sound("laser.ogg")

        def on_key_press(self, key, modifiers):
            # If the user hits  the space bar, play the sound that we loaded
            if key == arcade.key.SPACE:
                arcade.play_sound(self.laser_sound)

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        self.set_mouse_visible(False)

        arcade.set_background_color((8, 13, 38))
        # Create ball
        self.ball = Ball(50, 50, 0, 0, 25, arcade.color.BRIGHT_PINK)
        joysticks = arcade.get_joysticks()

        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.position_x = x
        self.ball.position_y = y

    def on_key_press(self, symbol: int, modifiers: int):
        self.ball.position_x = x
        self.ball.position_y = y

    def update(self, delta_time):
        self.ball.update()

        def on_key_press(self, key, modifiers):
            if key == arcade.key.LEFT:
                self.ball.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.ball.change_x = MOVEMENT_SPEED
            elif key == arcade.key.UP:
                self.ball.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.ball.change_y = -MOVEMENT_SPEED

        def on_key_release(self, key, modifiers):
            """ Called whenever a user releases a key. """
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.ball.change_x = 0
            elif key == arcade.key.UP or key == arcade.key.DOWN:
                self.ball.change_y = 0
        # Update the position according to the game controller
        if self.joystick:
            # "dead zone"
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = self.joystick.x * MOVEMENT_SPEED

            # "dead zone"
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball.change_y = 0
            else:
                self.ball.change_y = -self.joystick.y * MOVEMENT_SPEED

        self.ball.update()
# Monkey eating bananas


def main():
    window = MyGame(640, 480, "The bouncy ball")
    arcade.run()


main()


import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

WIDTH = 20
HEIGHT = 20
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):

        #Set up the application.

        super().__init__(width, height)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        #Render the screen.
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):

        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        # Row and Column counting code
        count = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    count += 1
        print("Total count", count)

        for row in range(ROW_COUNT):
            count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    count += 1
            print("Row", row, "has", count, "Cells selected")

        for column in range(COLUMN_COUNT):
            count = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    count += 1
            print("Column", column, "has", count, "Cells selected")

        # Continous Count
        continuous_count = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    continuous_count += 1

                elif continuous_count > 2:
                    print("There are", continuous_count, "continuous blocks "
                                                          "selected in row", row, "and column", column, ".")
                    continuous_count = 0

            if continuous_count > 2:
                print("There are", continuous_count, "continuous blocks "
                                                      "selected in row", row, "and column", column, ".")

            continuous_count = 0

            # Selecting green
            GREEN = 0
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    if self.grid[row][column] == 1:
                        GREEN += 1



def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()

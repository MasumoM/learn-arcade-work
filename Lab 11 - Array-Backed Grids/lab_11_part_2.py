import arcade

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

    def init(self, width, height):
        """
        Set up the application.
        """
        super().init(width, height)
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)
def on_draw(self):
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
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

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        GREEN = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    GREEN += 1
        print("Total of", GREEN, "cells are selected.")

        ROW = ROW_COUNT
        for row in range(ROW_COUNT):
            if self.grid[row] == 1:
                GREEN += 1
                ROW += 1
        print("Row", ROW, "has", GREEN, "cells selected.")

        COLUMN = COLUMN_COUNT
        for column in range(COLUMN_COUNT):
            if self.grid[row] == 1:
                GREEN += 1
                COLUMN += 1
        print("Column", COLUMN, "has", GREEN, "cells selected.")

        continuous_count = 0
        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.gris[row] == 1:
                continuous_count += 1

        if row < ROW_COUNT and column < COLUMN_COUNT:
                if self.grid[row] == 0:
                    if continuous_count > 2:
                        print("There are", continuous_count, "continuous blocks selected in row",
                              ROW, "and column", COLUMN, ".")

def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()

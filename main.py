import arcade

WIDTH = 1200
HEIGHT = 700
TITLE = "Tanks"

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("background.png")

    def on_draw(self):
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT, self.bg)
game = Game(width=WIDTH, height=HEIGHT, title=TITLE)


arcade.run()

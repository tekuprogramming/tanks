import arcade
import green_tank

WIDTH = 1200
HEIGHT = 700
TITLE = "Tanks"

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.bg = arcade.load_texture("background.png")

        # sprites
        self.green_tank = green_tank.Green_Tank()  # sprite tank

        # fields
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT, self.bg)
        self.green_tank.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.green_tank.change_angle = 2.5
            self.left_pressed = True
            self.right_pressed = False

        if key == arcade.key.RIGHT:
            self.green_tank.change_angle = -2.5
            self.right_pressed = True
            self.left_pressed = False

        if key == arcade.key.UP:
            self.green_tank.change_x = 4
            self.green_tank.change_y = 4
            self.up_pressed = True
            self.down_pressed = False

        if key == arcade.key.DOWN:
            self.green_tank.change_x = -3
            self.green_tank.change_y = -3
            self.down_pressed = True
            self.up_pressed = False

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT and not self.right_pressed:
            self.green_tank.change_angle = 0

        if key == arcade.key.RIGHT and not self.left_pressed:
            self.green_tank.change_angle = 0

        if key == arcade.key.UP and not self.down_pressed:
            self.green_tank.change_x = 0
            self.green_tank.change_y = 0

        if key == arcade.key.DOWN and not self.up_pressed:
            self.green_tank.change_x = 0
            self.green_tank.change_y = 0

    def update(self, delta_time):
        self.green_tank.update()

game = Game(WIDTH, HEIGHT, TITLE)
arcade.run()

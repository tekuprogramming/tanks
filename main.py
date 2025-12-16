import arcade
import green_tank

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("background.png")
        # sprites
        self.green_tank = green_tank.Green_Tank()  # sprite tank
        self.green_base = tank_base.Base("green_base.png", self, (255, 255, 0))
        self.red_base = tank_base.Base("red_base.png", self, (255, 165, 0))
        # sprites list
        self.bullet_list = arcade.SpriteList()
        # fields
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.place()

    def on_draw(self):
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT, self.bg)
        self.green_tank.draw()
        self.bullet_list.draw()
        self.red_base.draw()
        self.green_base.draw()

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
        if key == arcade.key.SPACE:
            bullet = tank_bullet.Bullet( "green_bullet.png", self.green_tank)
            self.bullet_list.append(bullet)
            
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
        self.bullet_list.update()

    def place(self):
        self.green_base.center_x = 90
        self.green_base.center_y = 190

        self.red_base.center_x = 1035
        self.red_base.center_y = 350

game = Game(width=WIDTH, height=HEIGHT, title=TITLE)
arcade.run()


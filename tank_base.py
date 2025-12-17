import arcade
from constants import *

class Base(arcade.Sprite):
    def __init__(self, image, window, color):
        super().__init__(image, 1.7)
        self.window = window
        self.color = color
        self.shots = 0

    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 320, 250, 15, (255, 0, 0), 3) # drawing life bar
        self.indent = self.shots * 25
        arcade.draw_rectangle_filled(self.center_x - self.indent / 2, self.center_y + 320, 250 - self.indent, 9, (98, 252, 3)) # fills in the life bar

    def update(self):
        hit = arcade.check_for_collision_with_list(self, self.window.bullet_list)
        for i in hit:
            i.kill()
            self.shots += 1

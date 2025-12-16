import arcade
from constants import *

class Bullet(arcade.Sprite):
    def __init__(self, image, tank):
        super().__init__(image, 0.1)
        self.center_x = tank.center_x
        self.center_y = tank.center_y
        self.angle = tank.angle
        self.change_x = 12 * tank.part_x
        self.change_y = 12 * tank.part_y

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left > WIDTH or self.right < 0 or self.top < 0 or self.bottom > HEIGHT: # removes used bullets
            self.kill()
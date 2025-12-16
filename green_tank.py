import math
import arcade
from constants import *

class Green_Tank(arcade.Sprite):
    def __init__(self):
        super().__init__("green.png", 0.12)
        self.center_x = 90 # coordinate x for tank
        self.center_y = 190 # coordinate y for tank
        self.activate = True

    def update(self): # responsible for movements of the character
        if self.activate:
            self.angle += self.change_angle # rotation angle for tank will change
            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            self.center_x += self.part_x * self.change_x # x position of tank will change
            self.center_y += self.part_y * self.change_y # y position of tank will change



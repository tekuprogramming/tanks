import arcade
from constants import *

class Base(arcade.Sprite):
    def __init__(self, image, window, color):
        super().__init__(image, 1.7)
        self.window = window
        self.color = color
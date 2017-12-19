from tkinter import *
from model_character import *

class Hero(Character):

    def __init__(self, map, random_num = 0, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0):
        super().__init__(random_num, char_x, char_y, hp, dp, sp)
        self.hp = self.hp * 3 + 20
        self.dp = self.dp * 2
        self.sp = self.sp + 5
        self.image = PhotoImage(file = 'hero-down.png')
        self.map = map
    
    def move_up(self):
        self.char_y = self.char_y - 72
    
    def move_down(self):
        self.char_y = self.char_y + 72

    def move_right(self):
        self.char_x = self.char_x + 72
    
    def move_left(self):
        self.char_x = self.char_x - 72

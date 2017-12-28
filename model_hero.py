from tkinter import *
from model_character import *

class Hero(Character):

    def __init__(self, random_num):
        super().__init__(random_num, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0)
        self.hp = self.hp * 3 + 20
        self.dp = self.dp * 2
        self.sp = self.sp + 5
        self.image = PhotoImage(file = 'hero-down.png')
        self.img_up = PhotoImage(file = 'hero-up.png')
        self.img_down = PhotoImage(file = 'hero-down.png')
        self.img_right = PhotoImage(file = 'hero-right.png')
        self.img_left = PhotoImage(file = 'hero-left.png')
    
    def move_up(self):
        self.char_y = self.char_y - 72
        self.image = self.img_up
    
    def move_down(self):
        self.char_y = self.char_y + 72
        self.image = self.img_down
        
    def move_right(self):
        self.char_x = self.char_x + 72
        self.image = self.img_right      
    
    def move_left(self):
        self.char_x = self.char_x - 72
        self.image = self.img_left       

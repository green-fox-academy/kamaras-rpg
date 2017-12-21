import random
from tkinter import *
from model_character import *

class Monster(Character):

    def __init__(self, random_num = 0, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0):
        super().__init__(random_num, char_x, char_y, hp, dp, sp)
        self.lvl_number = 1
        self.hp = 2 * self.lvl_number * self.hp
        self.dp = int((self.lvl_number / 2) * self.dp)
        self.sp = self.lvl_number * self.sp
        self.image = PhotoImage(file = 'skeleton.png')
    
    def move_monster(self):
        if random.randint(1, 4) == 1 and self.char_y + 576 > 38:
            self.char_y = self.char_y - 72
        if random.randint(1, 4) == 2 and self.char_y + 576 < 610:
            self.char_y = self.char_y + 72
        if random.randint(1, 4) == 3 and self.char_x + 72 < 610:
            self.char_x = self.char_x + 72
        if random.randint(1, 4) == 4 and self.char_x + 72 > 38:
            self.char_x = self.char_x - 72

class Boss(Monster):

    def __init__(self, random_num = 0, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0):
        super().__init__(random_num, char_x, char_y, hp, dp, sp)
        self.lvl_number = 1
        self.hp = self.hp + self.lvl_number
        self.dp = self.dp + self.lvl_number
        self.sp = self.sp * self.lvl_number + self.lvl_number
        self.image = PhotoImage(file = 'boss.png')

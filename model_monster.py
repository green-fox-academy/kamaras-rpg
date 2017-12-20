from tkinter import *
from model_character import *

class Monster(Character):

    def __init__(self, random_num = 0, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0):
        super().__init__(random_num, char_x, char_y, hp, dp, sp)
        self.lvl_number = 1
        self.hp = 2 * self.lvl_number * self.hp
        self.dp = int((self.lvl_number / 2) * self.dp)
        self.sp = self.lvl_number * self.sp
        # self.image = PhotoImage(file = 'skeleton.png')

class Boss(Monster):

    def __init__(self, random_num = 0, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0):
        super().__init__(random_num, char_x, char_y, hp, dp, sp)
        self.lvl_number = 1
        self.hp = self.hp
        self.dp = self.dp
        self.sp = self.sp
        # self.image = PhotoImage(file = 'boss.png')

monster = Monster()
print(monster.hp)
print(monster.dp)
print(monster.sp)
print('Random number:', monster.random_num)
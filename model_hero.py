from model_character import *

class Hero(Character):

    def __init__(self, random_num = 0, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0):
        super().__init__(random_num, char_x, char_y, hp, dp, sp)
        self.hp = self.hp * 3 + 20
        self.dp = self.dp * 2
        self.sp = self.sp + 5
        self.image = PhotoImage(file = 'hero-down.png')
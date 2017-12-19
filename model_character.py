import random

class Character():

    def __init__(self, random_num = 0, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0):
        self.random_num = random.randint(1, 6)
        self.char_x = char_x
        self.char_y = char_y
        self.hp = self.random_num
        self.dp = self.random_num
        self.sp = self.random_num

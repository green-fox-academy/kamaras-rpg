import random

class Character():

    main_random = random.randint(1, 6)

    def __init__(self, char_x = 38, char_y = 38, hp = 0, dp = 0, sp = 0, random_num = main_random):
        self.char_x = char_x
        self.char_y = char_y
        self.random_num = self.main_random
        self.hp = self.random_num
        self.dp = self.random_num
        self.sp = self.random_num

from tkinter import *

class Tile():

    def __init__(self):
        self.image = image
        self.size = 72
        self.type = type
        self.tile_x = tile_x
        self.tile_y = tile_y

class Floor(Tile):

    def __init__(self):
        super().__init__(self)
        self.image = PhotoImage(file = 'floor_tile.png')

class Wall(Tile):

    def __init__(self):
        super().__init__(self)
        self.image = PhotoImage(file = 'wall_tile.png')

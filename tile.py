from tkinter import *

class Tile():

    def __init__(self, size = 72, type = 'free', tile_x = 38, tile_y = 38):
        self.size = size
        self.type = type
        self.tile_x = tile_x
        self.tile_y = tile_y

class Floor(Tile):

    def __init__(self, size = 72, type = 'free', tile_x = 38, tile_y = 38):
        super().__init__(size, type, tile_x, tile_y)
        self.image = PhotoImage(file = 'floor_tile.png')

class Wall(Tile):

    def __init__(self, size = 72, type = 'closed', tile_x = 38, tile_y = 38):
        super().__init__(size, type, tile_x, tile_y)
        self.image = PhotoImage(file = 'wall_tile.png')

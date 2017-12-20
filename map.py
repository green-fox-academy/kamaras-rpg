from tkinter import *
from tile import *

class Map():

    def __init__(self):
        pass

    def read(self):
        temp = open('grid.txt', 'r')
        grid = temp.readlines()
        temp.close()
        return grid

    def draw_tile(self, canvas):
        global floor1
        floor1 = Floor()
        global wall1
        wall1 = Wall()
        grid = self.read()
        walls = []
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == '0':
                    canvas.create_image(floor1.tile_x + i * 72, floor1.tile_y + j * 72, image = floor1.image)
                elif grid[j][i] == '1':
                    canvas.create_image(wall1.tile_x + i * 72, wall1.tile_y + j * 72, image = wall1.image)
                    one_wall = []
                    one_wall.append(wall1.tile_x + i * 72)
                    one_wall.append(wall1.tile_y + j * 72)
                    walls.append(one_wall)
        return walls

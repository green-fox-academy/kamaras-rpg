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
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == '0':
                    canvas.create_image(floor1.tile_x + i * 72, floor1.tile_y + j * 72, image = floor1.image)
                elif grid[j][i] == '1':
                    canvas.create_image(wall1.tile_x + i * 72, wall1.tile_y + j * 72, image = wall1.image)

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()

map = Map()
map.draw_tile(canvas)
root.mainloop()



########################
# without global

# from tkinter import *
# from tile import *

# class Map():

#     def __init__(self):
#         pass

#     def draw_tile(self, canvas, floor1):
#         self.tile = canvas.create_image(floor1.tile_x, floor1.tile_y, image = floor1.image)

# root = Tk()
# canvas = Canvas(root, width = 720, height = 720)
# canvas.pack()

# floor1 = Floor()
# map = Map()
# map.draw_tile(canvas, floor1)
# root.mainloop()

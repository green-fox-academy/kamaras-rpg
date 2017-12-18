from tkinter import *
from tile import *

class Map():

    def __init__(self):
        pass

    def draw_tile(self, canvas):
        global floor1
        floor1 = Floor()
        global wall1
        wall1 = Wall()
        grid = [
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        ]
        for line in grid:
            for i in range(10):
                if line[i] == 0:
                    self.floor = canvas.create_image(floor1.tile_x + i * 72, floor1.tile_y, image = floor1.image)
                else:
                    self.wall = canvas.create_image(wall1.tile_x + i * 72, wall1.tile_y + 72, image = wall1.image)

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

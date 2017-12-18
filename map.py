from tkinter import *
from tile import *

class Map():

    def __init__(self):
        pass

    def draw_tile(self, canvas, floor1):
        self.tile = canvas.create_image(floor1.tile_x, floor1.tile_y, image = floor1.image)

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()

floor1 = Floor()
map = Map()
map.draw_tile(canvas, floor1)
root.mainloop()

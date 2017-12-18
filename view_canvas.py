from tkinter import *

class Tile():

    def __init__(self, canvas):
        self.canvas = canvas
        self.size = 72
        self.base_xy = 38
        self.tile_type = ''
        self.image = ''
    
# class Floor(Tile):
    
#     def __init__(self, canvas):
#         super().__init__(self)
#         self.image = PhotoImage(file = 'floor_tile.png')
    
    def draw_floor(self):
        self.img_floor = PhotoImage(file = 'floor_tile.png')
        for i in range(0, self.size * 10, self.size):
            for j in range(0, self.size * 10, self.size):
                self.floor = self.canvas.create_image(self.base_xy + i, self.base_xy + j, image = self.img_floor)
    
    def draw_wall(self):
        self.img_wall = PhotoImage(file = 'wall_tile.png')
        self.wall = self.canvas.create_image(110, 110, image = self.img_wall)

root = Tk()
my_canvas = Canvas(root, width = 720, height = 720)
my_canvas.pack()

object = Tile(my_canvas)
object.draw_floor()
object.draw_wall()

root.mainloop()
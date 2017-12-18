from tkinter import *
from tile import *

class Map():

    def __init__(self):
        pass

    def draw_main(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 720, height = 720)
        self.canvas.pack()
        self.root.mainloop()

map = Map()
map.draw_main()
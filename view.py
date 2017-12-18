from tkinter import *

class Map():

    def __init__(self):
        pass
    
    def draw_main(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 720, height = 720)
        self.img = PhotoImage(file = 'floor_tile.png')
        self.image = self.canvas.create_image(100, 100, image = self.img)
        self.canvas.pack()
        self.root.mainloop()

object = Map()
object.draw_main()
from tkinter import *

class Map():

    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw_main(self):
        self.img = PhotoImage(file = 'floor_tile.png')
        for i in range(0, 720, 72):
            for j in range(0, 720, 72):
                self.image = self.canvas.create_image(38 + i, 38 + j, image = self.img)

root = Tk()
my_canvas = Canvas(root, width = 720, height = 720)
my_canvas.pack()

object = Map(my_canvas)
object.draw_main()

root.mainloop()
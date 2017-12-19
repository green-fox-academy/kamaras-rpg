from map import *

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()

map = Map()
map.draw_tile(canvas)
root.mainloop()
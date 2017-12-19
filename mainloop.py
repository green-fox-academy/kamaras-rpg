from map import *
from model_hero import *

root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()

map = Map()
map.draw_tile(canvas)

my_hero = Hero()
my_hero.draw_hero(canvas)

root.mainloop()
from tkinter import *
from map import *
from model_hero import *

root = Tk()
canvas = Canvas(root, width = 720, height = 720)

map = Map()
map.draw_tile(canvas)

my_hero = Hero(canvas)

canvas.bind('<KeyPress>', my_hero.move_by_keys)
canvas.pack()
canvas.focus_set()

my_hero.draw_hero()

root.mainloop()

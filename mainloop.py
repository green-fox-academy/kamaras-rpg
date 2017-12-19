from tkinter import *
from map import *
from model_hero import *

root = Tk()
canvas = Canvas(root, width = 720, height = 720)

map = Map()
map.draw_tile(canvas)

my_hero = Hero(canvas, map)

def draw_hero():
    map.draw_tile(canvas)
    canvas.create_image(my_hero.char_x, my_hero.char_y, image = my_hero.image)

def move_by_keys(e):
    if e.keycode == 38:
        my_hero.move_up()
    elif e.keycode == 40:
        my_hero.move_down()
    elif e.keycode == 39:
        my_hero.move_right()
    elif e.keycode == 37:
        my_hero.move_left()
    draw_hero()

canvas.bind('<KeyPress>', move_by_keys)
canvas.pack()
canvas.focus_set()

draw_hero()

root.mainloop()

from tkinter import *
from map import *
from model_hero import *

root = Tk()
canvas = Canvas(root, width = 720, height = 720)

map = Map()
map.draw_tile(canvas)
temp_walls = map.draw_tile(canvas)

my_hero = Hero(canvas)

def draw_hero():
    map.draw_tile(canvas)
    canvas.create_image(my_hero.char_x, my_hero.char_y, image = my_hero.image)

def move_by_keys(e):
    if e.keycode == 38 and my_hero.char_y > 38 and [my_hero.char_x, my_hero.char_y - 72] not in temp_walls:
        my_hero.move_up()
    elif e.keycode == 40 and my_hero.char_y < 682 and [my_hero.char_x, my_hero.char_y + 72] not in temp_walls:
        my_hero.move_down()
    elif e.keycode == 39 and my_hero.char_x < 682 and [my_hero.char_x + 72, my_hero.char_y] not in temp_walls:
        my_hero.move_right()
    elif e.keycode == 37 and my_hero.char_x > 38 and [my_hero.char_x - 72, my_hero.char_y] not in temp_walls:
        my_hero.move_left()
    draw_hero()

canvas.bind('<KeyPress>', move_by_keys)
canvas.pack()
canvas.focus_set()

draw_hero()

root.mainloop()

# Lucy Langenberg
# I am going to paint a pretty picture

from cs1lib import *

def chicka_chicka_boom_boom():

    disable_stroke()

    # clear the background - egg-yolk yellow
    set_clear_color(1, 0.8, 0.01)
    clear()

    # add a pink border on the right/top
    set_fill_color(1, 0.01, 0.6)
    draw_rectangle(0, 0, 400, 50)
    draw_rectangle(345, 0, 55, 400)

    # draw yellow polka dots in the top border
    set_fill_color(1, 0.8, 0.01)
    x_coord = 0
    y_coord = 10
    while x_coord <= 400:
        draw_circle(x_coord, y_coord + 25, 7)
        draw_circle(x_coord + 25, y_coord, 7)
        x_coord = x_coord + 50

    # draw yellow polka dots in the right border
    x_coord = 360
    y_coord = 70
    while y_coord <= 400:
        draw_circle(x_coord, y_coord + 25, 7)
        draw_circle(x_coord + 25, y_coord, 7)
        y_coord = y_coord + 50

    # add brown trunk
    set_fill_color(0.3, 0.1, 0)
    draw_rectangle(15, 250, 70, 150)

    # add light green leaf
    set_fill_color(0.58, 0.85, 0.42)
    draw_rectangle(0, 80, 110, 180)
    draw_triangle(3, 90, 63, 80, 30, 35)
    set_fill_color(1, 0.8, 0.01)
    draw_triangle(0, 110, 1, 50, 20, 150)
    draw_triangle(63, 80, 63, 120, 110, 80)

    # add turquoise leaf
    set_fill_color(0.38, 0.8, 0.47)
    draw_triangle(0, 260, 0, 200, 17, 260)

    # add blue leaf
    set_fill_color(0.03, 0.66, 0.53)
    draw_triangle(50, 260, 25, 180, 130, 200)
    draw_triangle(25, 180, 120, 120, 120, 200)
    draw_triangle(120, 120, 120, 200, 135, 145)
    set_fill_color(0.58, 0.85, 0.42)
    draw_triangle(25, 180, 70, 170, 45, 80)
    draw_rectangle(55, 120, 35, 35)

    # draw foreground leaf
    set_fill_color(0.24, 0.75, 0.5)
    draw_triangle(50, 260, 115, 200, 200, 210)
    draw_triangle(195, 205, 250, 280, 50, 260)
    draw_circle(154, 224, 45)
    set_fill_color(1, 0.8, 0.01)
    # this is the point at which I got lazy... and also figured I should eat something

    # add coconuts
    set_fill_color(0.8, 0.23, 0.3)
    draw_circle(85, 290, 30)
    draw_circle(120, 230, 30)


start_graphics(chicka_chicka_boom_boom)
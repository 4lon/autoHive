from math import sin, cos, tan, radians
import tkinter as tk
from parts import Joint


def createLatticeOld(canvas, dim_x, dim_y):
    line_length = min(canvas.winfo_width() / (dim_x - 2), canvas.winfo_height() / ((dim_y - 2) * cos(radians(30))))
    position = [canvas.winfo_width() / 2 - line_length * dim_x / 2, canvas.winfo_height() / 2 - line_length * dim_y / 2]
    start_x = canvas.winfo_width() / 2 - (line_length * (dim_x - 0.5) / 2)
    lattice = [[None] * dim_y] * dim_x
    for y in range(0, dim_y, 1):
        position[0] = start_x + (y % 2 * 0.5) * line_length
        position[1] += line_length * sin(radians(60))
        for x in range(0, dim_x, 1):
            lattice[x][y] = Joint([x, y], line_length, position, canvas)
            position[0] += line_length


def create_lattice(canvas, line_length):
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    mid = height / 2
    offset = 0

    while offset <= mid:
        canvas.create_line(0, mid + offset, width, mid + offset, width=3, fill='#424242')
        canvas.create_line(0, mid - offset, width, mid - offset, width=3, fill='#424242')
        offset += line_length * cos(radians(30))

    mid = width / 2
    mid_width = (height / 2) / tan(radians(60))
    offset = 0

    while offset <= mid + mid_width:
        canvas.create_line(mid - mid_width + offset, 0, mid + mid_width + offset, height, width=3, fill='#424242')
        canvas.create_line(mid - mid_width - offset, 0, mid + mid_width - offset, height, width=3, fill='#424242')
        canvas.create_line(mid - mid_width + offset, height, mid + mid_width + offset, 0, width=3, fill='#424242')
        canvas.create_line(mid - mid_width - offset, height, mid + mid_width - offset, 0, width=3, fill='#424242')
        offset += line_length


def find_triangle(event):
    print(event)


def gui():
    root = tk.Tk()
    root.title("autoHive")

    w = 500
    h = 400
    line_length = 60
    canvas = tk.Canvas(root, width=w, height=h, bg='#121212')
    canvas.pack()

    root.update()
    create_lattice(canvas, line_length)

    canvas.bind('<Button-1>', find_triangle)
    canvas.bind('<B1-Motion>', find_triangle)

    root.mainloop()

from math import sin, cos, radians
import tkinter as tk
from parts import Joint


def createLattice(canvas, dim_x, dim_y):
    line_length = min(canvas.winfo_width() / (dim_x - 2), canvas.winfo_height() / ((dim_y - 2)*cos(radians(30))))
    position = [canvas.winfo_width() / 2 - line_length * dim_x / 2, canvas.winfo_height() / 2 - line_length * dim_y / 2]
    start_x = canvas.winfo_width() / 2 - (line_length * (dim_x - 0.5) / 2)
    lattice = [[None] * dim_y] * dim_x
    for y in range(0, dim_y, 1):
        position[0] = start_x + (y % 2 * 0.5) * line_length
        position[1] += line_length * sin(radians(60))
        for x in range(0, dim_x, 1):
            lattice[x][y] = Joint([x,y], line_length, position, canvas)
            position[0] += line_length


def gui():
    root = tk.Tk()
    root.title("autoHive")

    w = 500
    h = 400
    cv = tk.Canvas(root, width=w, height=h, bg='#121212')
    cv.pack()

    root.update()
    createLattice(cv, 10, 10)

    root.mainloop()
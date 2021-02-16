from math import sin, cos, tan, radians
import tkinter as tk
from parts import Joint


def createLatticeOld(canvas, dim_x, dim_y):
    line_length = min(canvas.winfo_width() / (dim_x - 2), canvas.winfo_height() / ((dim_y - 2) * sin(radians(60))))
    position = [canvas.winfo_width() / 2 - line_length * dim_x / 2, canvas.winfo_height() / 2 - line_length * dim_y / 2]
    start_x = canvas.winfo_width() / 2 - (line_length * (dim_x - 0.5) / 2)
    lattice = [[None] * dim_y] * dim_x
    for y in range(0, dim_y, 1):
        position[0] = start_x + (y % 2 * 0.5) * line_length
        position[1] += line_length * sin(radians(60))
        for x in range(0, dim_x, 1):
            lattice[x][y] = Joint([x, y], line_length, position, canvas)
            position[0] += line_length


class Lattice(tk.Canvas):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._line_length = 60

    def create(self):
        width = self.winfo_width()
        height = self.winfo_height()

        mid = height / 2
        offset = 0

        while offset <= mid:
            self.create_line(0, mid + offset, width, mid + offset, width=3, fill='#424242')
            self.create_line(0, mid - offset, width, mid - offset, width=3, fill='#424242')
            offset += self._line_length * sin(radians(60))

        mid = width / 2
        mid_width = (height / 2) / tan(radians(60))
        offset = 0

        while offset <= mid + mid_width:
            self.create_line(mid - mid_width + offset, 0, mid + mid_width + offset, height, width=3, fill='#424242')
            self.create_line(mid - mid_width - offset, 0, mid + mid_width - offset, height, width=3, fill='#424242')
            self.create_line(mid - mid_width + offset, height, mid + mid_width + offset, 0, width=3, fill='#424242')
            self.create_line(mid - mid_width - offset, height, mid + mid_width - offset, 0, width=3, fill='#424242')
            offset += self._line_length


def find_triangle(event):
    w = 500 / 2
    h = 400 / 2
    # print(type(event.widget))
    # event.widget.create_polygon([[0, 0], [0, 100], [100, 0]], fill='#33D4FF')
    # y = mx + c
    c = 0
    # ms = [0, sin(radians(60)), -sin(radians(60))]
    # for m in ms:
    #     y = m*(event.x-w) + c
    # print(y, -(event.y-h))
    # x = ((event.y - h) - c) / m
    # side = (event.x - w - x)/abs(event.x - w - x)
    # print(side)
    x = event.x - (event.widget.winfo_width() / 2)
    y = -(event.y - (event.widget.winfo_height() / 2))

    line_length = 60
    print(y / (line_length * sin(radians(60))))
    print(x / line_length)

    # event.widget.create_polygon([[line_length, ]])


def gui():
    root = tk.Tk()
    root.title("autoHive")

    w = 500
    h = 400
    lattice = Lattice(root, width=w, height=h, bg='#121212')
    lattice.pack()

    root.update()
    lattice.create()

    lattice.bind('<Button-1>', find_triangle)
    lattice.bind('<B1-Motion>', find_triangle)

    root.mainloop()

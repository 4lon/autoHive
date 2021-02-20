from math import sin, tan, radians, floor, ceil
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
        self._width = None
        self._height = None
        self._clicked = False
        self._selected = {}
        self._colours = {True: '#33D4FF',
                         False: '#424242'}

    def create(self):
        self._width = self.winfo_width()
        self._height = self.winfo_height()

        mid = self._height / 2
        offset = 0

        while offset <= mid:
            self.create_line(0, mid + offset, self._width, mid + offset, width=3, fill='#424242')
            self.create_line(0, mid - offset, self._width, mid - offset, width=3, fill='#424242')
            offset += self._line_length * sin(radians(60))

        mid = self._width / 2
        mid_width = (self._height / 2) / tan(radians(60))
        offset = 0

        while offset <= mid + mid_width:
            self.create_line(mid - mid_width + offset, 0, mid + mid_width + offset, self._height, width=3,
                             fill='#424242')
            self.create_line(mid - mid_width - offset, 0, mid + mid_width - offset, self._height, width=3,
                             fill='#424242')
            self.create_line(mid - mid_width + offset, self._height, mid + mid_width + offset, 0, width=3,
                             fill='#424242')
            self.create_line(mid - mid_width - offset, self._height, mid + mid_width - offset, 0, width=3,
                             fill='#424242')
            offset += self._line_length

    def conv_to_canvas(self, x, y):
        return [(x + (self._width / 2)), (-y + (self._height / 2))]

    def conv_to_regular(self, x, y):
        return [(x - (self._width / 2)), -(y - (self._height / 2))]

    def find_triangle(self, event):
        x, y = self.conv_to_regular(event.x, event.y)
        m1 = self._line_length * sin(radians(60)) / (self._line_length / 2)
        m2 = -m1
        c1 = c2 = 0

        initial = side = int((x - ((y - c2) / m2)) / abs(x - ((y - c2) / m2)))
        while initial == side:
            c2 += 2 * side * self._line_length * sin(radians(60))
            side = int((x - ((y - c2) / m2)) / abs(x - ((y - c2) / m2)))

        left_column = (int(c2 / (2 * self._line_length * sin(radians(60)))))

        initial = side = int((x - ((y - c1) / m1)) / abs(x - ((y - c1) / m1)))
        while initial == side:
            c1 -= 2 * side * self._line_length * sin(radians(60))
            side = int((x - ((y - c1) / m1)) / abs(x - ((y - c1) / m1)))

        right_column = (int(-c1 / (2 * self._line_length * sin(radians(60)))))

        if (y / (sin(radians(60)) * self._line_length)) > 0:
            row = int(ceil(y / (sin(radians(60)) * self._line_length)))
        else:
            row = int(floor(y / (sin(radians(60)) * self._line_length)))
        return f"{left_column},{right_column},{row}"

    def select_triangle(self, key):
        if not self._selected.get(key):
            if self._clicked:
                self._selected[key] = self.create_polygon(self.find_points(key), fill=self._colours[True])
        else:
            if self._clicked:
                self.itemconfig(self._selected[key], fill=self._colours[True])
            else:
                self.delete(self._selected[key])
                self._selected.pop(key)

    def find_points(self, key):
        location = key.split(',')
        for i in range(0, 3, 1):
            location[i] = int(location[i])
            if location[i] >= 0:
                location[i] -= 1
        if (location[2] % 2) == 0:
            if (location[0] + location[1]) % 2 == 0:
                type = 'upper'
            else:
                type = 'lower'
        else:
            if (location[0] + location[1]) % 2 == 0:
                type = 'lower'
            else:
                type = 'upper'
        m = [-self._line_length * sin(radians(60)) / (self._line_length / 2),
             self._line_length * sin(radians(60)) / (self._line_length / 2), 0]
        c = [0, 0, 0]
        if type == 'upper':
            location[0] += 1
        if type == 'lower':
            location[1] += 1
            location[2] += 1

        c[0] = location[0] * 2 * self._line_length * sin(radians(60))
        c[1] = location[1] * -2 * self._line_length * sin(radians(60))
        c[2] = location[2] * self._line_length * sin(radians(60))

        return [self.conv_to_canvas((c[2] - c[0]) / m[0], c[2]), self.conv_to_canvas((c[2] - c[1]) / m[1], c[2]),
                self.conv_to_canvas((c[1] - c[0]) / (m[0] - m[1]), m[0] * (c[1] - c[0]) / (m[0] - m[1]) + c[0])]

    def enable(self, event):
        key = self.find_triangle(event)
        if not self._selected.get(key):
            self._clicked = True
        else:
            self._clicked = False
        self.select_triangle(key)

    def cont(self, event):
        key = self.find_triangle(event)
        self.select_triangle(key)

    def disable(self, event):
        self._clicked = False


def gui():
    root = tk.Tk()
    root.title("autoHive")

    w = 800
    h = 600
    lattice = Lattice(root, width=w, height=h, bg='#121212')
    lattice.pack()

    root.update()
    lattice.create()

    lattice.bind('<Button-1>', lattice.enable)
    lattice.bind('<B1-Motion>', lattice.cont)
    lattice.bind('<ButtonRelease-1>', lattice.disable)

    root.mainloop()

from math import sin, cos, radians
import tkinter as tk
from parts import Joint


def overShape(event):
    print(event)


def makeRectangle(canvas, location, line_length, angle):
    points = [[location[0], location[1]], [None, None], [None, None], [None, None]]
    # position = location
    radius = 10
    angle -= 30
    points[0][0] += radius * cos(radians(angle))
    points[0][1] -= radius * sin(radians(angle))
    angle += 30
    points[0][0] += radius / 4 * cos(radians(angle))
    points[0][1] -= radius / 4 * sin(radians(angle))
    side_length = line_length - (2 * radius * (cos(radians(30)) + 0.25))
    sides = [side_length, radius] * 2
    for i in range(1, 4, 1):
        points[i][0] = points[i - 1][0] + sides[i - 1] * cos(radians(angle))
        points[i][1] = points[i - 1][1] - sides[i - 1] * sin(radians(angle))
        angle += 90

    canvas.create_polygon(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1],
                          points[3][0], points[3][1], fill="#424242", tag='rectangle')

    canvas.tag_bind('rectangle', '<Motion>', overShape)


def createLattice(canvas, dim_x, dim_y):
    line_length = min(canvas.winfo_width() / (dim_x - 2), canvas.winfo_height() / ((dim_y - 2)*cos(radians(30))))
    position = [canvas.winfo_width() / 2 - line_length * dim_x / 2, canvas.winfo_height() / 2 - line_length * dim_y / 2]
    start_x = canvas.winfo_width() / 2 - (line_length * (dim_x - 0.5) / 2)
    lattice = [[None] * dim_y] * dim_x
    for y in range(0, dim_y, 1):
        position[0] = start_x + (y % 2 * 0.5) * line_length
        position[1] += line_length * sin(radians(60))
        for x in range(0, dim_x, 1):
            lattice[x][y] = Joint("j"+str(x)+str(y), position, canvas)
            lattice[x][y].display()
            if x != 0:
                makeRectangle(canvas, position, line_length, 180)
            if y != 0:
                if not ((x == 0) and (y % 2 == 0)):
                    makeRectangle(canvas, position, line_length, 120)
                if not ((x == dim_x - 1) and (y % 2)):
                    makeRectangle(canvas, position, line_length, 60)
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
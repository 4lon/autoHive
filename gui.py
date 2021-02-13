from math import sin, cos, radians
import tkinter as tk


def overShape(event):
    print(event)


def makeHexagon(canvas, location):
    points = []
    radius = 10
    centre = location
    angle = 30
    for i in range(0, 6, 1):
        points.append([centre[0] + radius * cos(radians(angle)), centre[1] + radius * sin(radians(angle))])
        angle += 60

    canvas.create_polygon(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1],
                          points[3][0], points[3][1], points[4][0], points[4][1], points[5][0], points[5][1],
                          fill="red", tag='hexagon')

    canvas.tag_bind('hexagon', '<Motion>', overShape)


def lattice(canvas, dim_x, dim_y):
    padding = 0
    line_length = min(canvas.winfo_width() / (dim_x + 1), canvas.winfo_height() / (dim_y + 1))
    position = [0, 0]
    for i in range(0, dim_y, 1):
        position[0] = (line_length / 1.5) + padding + (i % 2 * 0.5) * line_length
        position[1] += line_length * sin(radians(60))
        for j in range(0, dim_x, 1):
            makeHexagon(canvas, position)
            position[0] += line_length


def gui():
    root = tk.Tk()
    root.title("autoHive")

    w = 400
    h = 400
    cv = tk.Canvas(root, width=w, height=h, bg='white')
    cv.pack()

    root.update()
    lattice(cv, 5, 5)

    root.mainloop()

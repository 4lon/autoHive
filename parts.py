from math import sin, cos, radians


class Part(object):
    def __init__(self, coords, canvas):
        super().__init__()
        self._coords = coords
        self._active = False
        self._polygon = None
        self._canvas = canvas
        self._colours = {True: '#33D4FF',
                         False: '#424242'}
        self.display()

    def display(self):
        self._polygon = self._canvas.create_polygon(self._points, fill=self._colours[self._active], tag=self._id)
        self._canvas.tag_bind(self._id, '<Button-1>', self.toggle)

    def toggle(self, event):
        self._active = not self._active
        self.recolour()

    def recolour(self):
        self._canvas.itemconfig(self._polygon, fill=self._colours[self._active])


class Joint(Part):
    def __init__(self, coords, line_length, location, canvas):
        self._location = location
        self._points = []
        self._radius = 5
        self._id = "j" + str(coords[0]) + str(coords[1])
        self._sides = {'E': Side(coords, line_length, canvas, location, 0),
                       'SE': Side(coords, line_length, canvas, location, -60),
                       'SW': Side(coords, line_length, canvas, location, -120)}
        angle = 30
        for i in range(0, 6, 1):
            self._points.append([self._location[0] + self._radius * cos(radians(angle)),
                                 self._location[1] + self._radius * sin(radians(angle))])
            angle += 60

        super().__init__(coords, canvas)


class Side(Part):
    def __init__(self, coords, line_length, canvas, location, angle):
        self._angle = angle

        points = [[location[0], location[1]], [None, None], [None, None], [None, None]]
        radius = 5
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

        self._id = "s" + str(angle) + str(coords[0]) + str(coords[1])
        self._points = points

        super().__init__(coords, canvas)

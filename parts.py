from math import sin, cos, radians


class Part(object):
    def __init__(self, canvas):
        super().__init__()
        self._active = False
        self._polygon = None
        self._canvas = canvas
        self._colours = {True: '#B8E2F2',
                         False: '#424242'}

    def toggle(self, event):
        self._active = not self._active
        self.recolour()

    def recolour(self):
        self._canvas.itemconfig(self._polygon, fill=self._colours[self._active])


class Joint(Part):
    def __init__(self, id, location, canvas):
        super().__init__(canvas)
        self._id = id
        self._points = []
        self._radius = 10
        self._location = location
        angle = 30
        for i in range(0, 6, 1):
            self._points.append([self._location[0] + self._radius * cos(radians(angle)),
                                 self._location[1] + self._radius * sin(radians(angle))])
            angle += 60

    def display(self):
        self._polygon = self._canvas.create_polygon(self._points, fill=self._colours[self._active], tag=self._id)
        self._canvas.tag_bind(self._id, '<Button-1>', self.toggle)


class Side(Part):
    def __init__(self):
        super().__init__()

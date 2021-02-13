from os import getcwd
import sys
from math import cos, sin, radians
from gui import gui

FREECADPATH = 'C:\\Program Files\\FreeCAD 0.18\\bin'  # path to your FreeCAD.so or FreeCAD.dll file
sys.path.append(FREECADPATH)


def demoHiveCreator():
    try:
        import FreeCAD
        import Import
        import Mesh
    except ValueError:
        print("FreeCAD not found")
    else:
        cwd = getcwd()
        name = "autoHive"
        doc = FreeCAD.newDocument(name)

        # faces = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female']
        # angles = [60, -60, -60, -60, -60, 60, -60, -60, -60, -60]
        # faces = ['male', 'male', 'female', 'female']
        # angles = [-120, -60, -120, -60]
        faces = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male',
                 'female', 'male', 'female', 'male', 'female', 'male', 'female']
        angles = [60, -60, -60, 60, 60, -60, -60, -60, -60, 60, -60, -60, 60, 60, -60, -60, -60, -60]

        i = 0
        angle = 0
        coords = [0, 0]
        side_length = (40.5 / (3 ** 0.5)) * 2

        for j in range(0, len(faces), 1):
            Import.insert(cwd + "\\models\\" + faces[int(i / 2)] + ".stp", name)
            doc.Objects[i].Placement = FreeCAD.Placement(FreeCAD.Vector(coords[0], coords[1], 0),
                                                         FreeCAD.Rotation(angle, 0, 0),
                                                         FreeCAD.Vector(0, 0, 0))
            Import.insert(cwd + "\\models\\" + str(angles[int(i / 2)]) + ".stp", name)
            doc.Objects[i + 1].Placement = FreeCAD.Placement(FreeCAD.Vector(coords[0], coords[1], 0),
                                                             FreeCAD.Rotation(angle, 0, 0),
                                                             FreeCAD.Vector(0, 0, 0))

            coords[0] += (side_length * cos(radians(angle + 60))) + (
                    side_length * cos(radians(angle + angles[int(i / 2)] - 60)))
            coords[1] += (side_length * sin(radians(angle + 60))) + (
                    side_length * sin(radians(angle + angles[int(i / 2)] - 60)))

            angle += angles[int(i / 2)]

            i += 2

        Mesh.export(doc.Objects, cwd + "\\" + name + ".stl")
        FreeCAD.closeDocument(name)


if __name__ == '__main__':
    gui()

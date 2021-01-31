from os import getcwd
import sys

FREECADPATH = 'C:\\Program Files\\FreeCAD 0.18\\bin'  # path to your FreeCAD.so or FreeCAD.dll file
sys.path.append(FREECADPATH)


def main():
    try:
        import FreeCAD
    except ValueError:
        print("FreeCAD not found")

    cwd = getcwd()
    name = "autoHive"
    doc = FreeCAD.newDocument(name)

    import Import
    types = ["male", "female", "male", "female", "male", "female", "joint120", "joint120", "joint120", "joint120",
             "joint120", "joint120"]

    for i in range(0, 12, 1):
        Import.insert(cwd + "\\models\\" + types[i] + ".stp", name)
        doc.Objects[i].Label = str(i)
        doc.Objects[i].Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(i * 60, 0, 0),
                                                     FreeCAD.Vector(0, 0, 0))
        # FreeCAD.Placement.move(doc.Objects[i].Placement, FreeCAD.Vector(2,0,0))

    import Mesh
    Mesh.export(doc.Objects, cwd + "\\" + name + ".stl")
    FreeCAD.closeDocument(name)


if __name__ == '__main__':
    main()

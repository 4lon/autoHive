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
    Doc = FreeCAD.newDocument("autoHive")
    Doc.saveAs(cwd + u"\\autoHive.FCStd")


if __name__ == '__main__':
    main()

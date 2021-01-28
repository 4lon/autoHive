from win32com.client import Dispatch, GetActiveObject, gencache, constants

def main():
    try:
        invApp = GetActiveObject('Inventor.Application')
    except:
        invApp = Dispatch('Inventor.Application')
        invApp.Visible = True

    mod = gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
    invApp = mod.Application(invApp)
    # invApp.SilentOperation = True

    # Create a new part
    invDoc = invApp.Documents.Add(constants.kPartDocumentObject, "", True)

    # Casting Document to PartDocument
    invPartDoc = mod.PartDocument(invDoc)

    compdef = invPartDoc.ComponentDefinition

    # Create a sketch
    xyPlane = compdef.WorkPlanes.Item(3)
    sketch = compdef.Sketches.Add(xyPlane)

    # Set Geometry variables
    tg = invApp.TransientGeometry
    lines = sketch.SketchLines

    # Draw Triangle
    line1 = lines.AddByTwoPoints(tg.CreatePoint2d(0, 0), tg.CreatePoint2d(4, 0))
    line2 = lines.AddByTwoPoints(line1.EndSketchPoint, tg.CreatePoint2d(4, 3))
    line3 = lines.AddByTwoPoints(line2.EndSketchPoint, line1.StartSketchPoint)

    # Draw slotted hole
    # Create the sketch points.
    points = sketch.SketchPoints
    arcs = sketch.SketchArcs
    pointArray = []
    pointArray.append(points.Add(tg.CreatePoint2d(0, 1), False))
    pointArray.append(points.Add(tg.CreatePoint2d(0, 0), False))
    pointArray.append(points.Add(tg.CreatePoint2d(0, -1), False))
    pointArray.append(points.Add(tg.CreatePoint2d(4, -1), False))
    pointArray.append(points.Add(tg.CreatePoint2d(4, 0), False))
    pointArray.append(points.Add(tg.CreatePoint2d(4, 1), False))
    # Draw the geometry.
    arc1 = arcs.AddByCenterStartEndPoint(
        pointArray[1], pointArray[0], pointArray[2])
    line1 = lines.AddByTwoPoints(pointArray[2], pointArray[3])
    arc2 = arcs.AddByCenterStartEndPoint(
        pointArray[4], pointArray[3], pointArray[5])
    line2 = lines.AddByTwoPoints(pointArray[5], pointArray[0])

    # Draw Rectangle
    rectangle = lines.AddAsTwoPointRectangle(
        tg.CreatePoint2d(0, 0), tg.CreatePoint2d(4, 3))

    # Extrude
    profile = sketch.Profiles.AddForSolid()
    extrudeDef = compdef.Features.ExtrudeFeatures.CreateExtrudeDefinition(
        profile, constants.kJoinOperation)
    extrudeDef.SetDistanceExtent(1, constants.kNegativeExtentDirection)
    extrude = compdef.Features.ExtrudeFeatures.Add(extrudeDef)

    # Close Document and Inventor
    # invPartDoc.Close(SkipSave=True)
    # invApp.Quit()

if __name__ == '__main__':
    main()
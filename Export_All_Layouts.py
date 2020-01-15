import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT")
for lyt in aprx.listLayouts():
    outName = r"C:\Users\kberg\Desktop" + "\\" + lyt.name + ".pdf"
    lyt.exportToPDF(outName)
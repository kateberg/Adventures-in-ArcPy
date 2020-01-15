# Adventures-in-ArcPy

### By Kate Berg

This is a collection of Python (ArcPy) scripts and resources for various GIS-related workflows.

## Table of Contents
[ArcGIS Pro | Export All Layouts](https://github.com/kateberg/Adventures-in-ArcPy/blob/master/README.md#arcgis-pro--export-all-layouts)


### ArcGIS Pro | Export All Layouts
```python
import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT")
for lyt in aprx.listLayouts():
    outName = r"C:\Users\kberg\Desktop" + "\\" + lyt.name + ".pdf"
    lyt.exportToPDF(outName)
```

import os
import json
import hou
from geoJSON import main
#HDA params
#geodata
#normalizecoordinate
#differentheight
#addpolygon
#HDA params

node = hou.pwd()
geo = node.geometry()

file = hou.ch('geodata')
differentheight = int(hou.ch('differentheight'))
addpolygon  = int(hou.ch('addpolygon'))

minx = 0
miny = 0

cb = main.CountryBoundaries(file, 'Ukraine')
boundaries = cb.getCountryBoundaries()
if(int(hou.ch('normalizecoordinate'))):
    minx = cb.getMinX()
    miny = cb.getMinY()

for ind, x in enumerate(boundaries):
    poly = geo.createPolygon()
    if(differentheight == 0):
        ind = 0
    for y in x:
        for z in y:
            pt = geo.createPoint()
            pt.setPosition(hou.Vector3(z[1] - miny, 0 + ind, z[0] - minx))
            if(addpolygon == 1):
                poly.addVertex(pt)
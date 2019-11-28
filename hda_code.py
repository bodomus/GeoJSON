import os
import json
import hou
from geoJSON import main

# HDA params
# geodata
# normalizecoordinate
# differentheight
# addpolygon
# countries
# HDA params

node = hou.pwd()
geo = node.geometry()

file = hou.ch('geodata')
differentheight = int(hou.ch('differentheight'))
addpolygon = int(hou.ch('addpolygon'))
country = hou.ch('countries')
print 'Country'
print (country)

minx = 0
miny = 0
if (country <> None):
    print (country)
    cb = main.CountryBoundaries(file, country)

    boundaries = cb.getCountryBoundaries()
    if (int(hou.ch('normalizecoordinate'))):
        minx = cb.getMinX()
        miny = cb.getMinY()

    for ind, x in enumerate(boundaries):
        poly = geo.createPolygon()
        if (differentheight == 0):
            ind = 0
        for y in x:
            for z in y:
                pt = geo.createPoint()
                pt.setPosition(hou.Vector3(z[1] - miny, 0 + ind, z[0] - minx))
                if (addpolygon == 1):
                    poly.addVertex(pt)




                    ###

                    # import os
                    # import json
                    # import hou
                    # from geoJSON import main
                    #
                    # file = hou.ch('geodata')
                    # boundaries = main.CountryBoundaries(file, 'Ukraine')
                    # countries = boundaries.getcountriesname()
                    # cc = []
                    # for con in countries:
                    #     cc.append(con['name'])
                    #     cc.append(con['name'] + ',' + con['shortname'])
                    #
                    # return cc
                ###
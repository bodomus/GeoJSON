import os
import json
import hou
import main

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
different_height = int(hou.ch('differentheight'))
add_polygon = int(hou.ch('addpolygon'))
country = hou.ch('countries')
print(country)

minx = 0
miny = 0
if country is not None:
    cb = main.CountryBoundaries(file, country)

    boundaries = cb.get_country_boundaries()
    if int(hou.ch('normalizecoordinate')):
        minx = cb.get_min_x()
        miny = cb.get_min_y()

    for ind, x in enumerate(boundaries):
        poly = geo.createPolygon()
        if different_height == 0:
            ind = 0
        for y in x:
            for z in y:
                pt = geo.createPoint()
                pt.setPosition(hou.Vector3(z[1] - miny, 0 + ind, z[0] - minx))
                if add_polygon == 1:
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

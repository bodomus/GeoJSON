### Learn python types
###
# from datapackage import Package
import os
import json
import hou

# package = Package('https://datahub.io/core/geo-countries/datapackage.json')
# print(package)
# print(package.resource_names)
class CountryBoundaries():
    def __init__(self, dataFile, countryName):
        self.dataFile = dataFile
        self.countryName = countryName
        self.geo = None

    def getCountryByName(self, items, name):
        for item in items:
            i = item['properties']
            if (i['ADMIN'] == name):
                return (i['ADMIN'], i['ISO_A3'], item['geometry'])
        return None

    def getGeometry(self, geo):
        return geo['coordinates']

    def prn(self):
        if(self.geo != None):
            print(self.geo)

    def getCountryBoundaries(self):
        if (not os.path.isfile(self.dataFile)):
            return (None, "Invalid file path.")
        with open(self.dataFile) as json_file:
            data = json.load(json_file)
            p = data['features']
            type = data['type']
            if (type != "FeatureCollection"):
                return (None, "Invalid format file")
            cName, cISO, cGeometry = self.getCountryByName(p, 'Ukraine')
            self.geo = self.getGeometry(cGeometry)[0]
            return self.geo
            # for idx, point in enumerate(g):
            #    c = point
            #    print('index:%d %f %f ' % (idx, c[0], c[1]))

    def createBoundaries(self):
        line = hou.node('/obj').createNode('geo').createNode('line')
        g = line.geometry()
        for item in self.geo[0]:
            p = g.createPoint()
            p.setPosition(hou.Vector3(item[0], item[0], 0))
        # line = hou.node('/obj').createNode('geo').createNode('line')
        # g = line.geometry().freeze()
        # p = g.points()[0]
        # p.setPosition(hou.Vector3(1, 0, 0))
        # p = g.points()[1]
        # p.setPosition(hou.Vector3(0, 0, 0))
        # pt2=g.createPoint()
        # pt2.setPosition(hou.Vector3(1, 1, 1))
        #
        # geo = line.geometry()
        # geo.clear()  # clear current geo
        # geo.merge(g)

        # pt0 = geo.createPoint()
        # pt0.setPosition(hou.Vector3(1, 0, 0))
        #
        # pt1 = geo.createPoint()
        # pt1.setPosition(hou.Vector3(0, 1, 0))
        # pt2 = geo.createPoint()
        # pt2.setPosition(hou.Vector3(0, 0, 1))
        # poly = geo.createPolygon()
        # poly.addVertex(pt0);
        # poly.addVertex(pt1);
        # poly.addVertex(pt2);

if __name__ == "__main__":
    import os
    import hou
    import json
    import hrpyc

    con, hou = hrpyc.import_remote_module()

    boundaries = CountryBoundaries('countries.geojson', 'Ukraine')
    boundaries.getCountryBoundaries()
    boundaries.prn()
    boundaries.createBoundaries()
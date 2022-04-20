### Learn python types
###
# from datapackage import Package
import os
import json
import geotest


# import hou


class CountryBoundaries:

    def __init__(self, dataFile, countryName):
        if not os.path.isfile(dataFile):
            raise hou.NodeError("The error occured. File does not exist. ")
        self.dataFile = dataFile
        self.countryName = countryName
        self.geo = None
        self.usedifferentheightforgroups = True

    # add in version 1.0.4
    def setdifferentheightflag(self, isUse):
        self.usedifferentheightforgroups = isUse

    def setcountryName(self, shortName):
        if (shortName <> None):
            cName, cISO, cGeometry = self.getCountryByShortName(shortName)
            self.countryName = cName

    # add in version 1.0.4
    def getdifferentheightflag(self):
        return self.usedifferentheightforgroups

    def getcountry(self):
        return self.countryName

    def getversion(self):
        return 'ver 1.0.5'

    def getcountriesnamefromfile(self, filename):
        if (not os.path.isfile(filename)):
            return (None, "Invalid file path.")
        with open(filename) as json_file:
            data = json.load(json_file)
        return data

    def getcountriesname(self):
        if (not os.path.isfile(self.dataFile)):
            return (None, "Invalid file path.")
        with open(self.dataFile) as json_file:
            data = json.load(json_file)

            p = data['features']
            type = data['type']
            if (type != "FeatureCollection"):
                return (None, "Invalid format file")
        list = []
        for item in p:
            i = item['properties']
            list.append({'name': i['ADMIN'], 'shortname': i['ISO_A3']})

        return list

    def getCountryByName(self, items, name):
        for item in items:
            i = item['properties']
            if (i['ADMIN'] == name):
                return (i['ADMIN'], i['ISO_A3'], item['geometry'])
        return None

    def getCountryByShortName(self, items, shortname):
        for item in items:
            i = item['properties']
            if (i['ISO_A3'] == shortname):
                return (i['ADMIN'], i['ISO_A3'], item['geometry'])
        return None

    def getMinX(self):
        min = 100000
        for items in self.geo:
            for x in items:
                for z in x:
                    if (type(z) is float):
                        if (z < min):
                            min = z
                    else:
                        if (z[0] < min):
                            min = z[0]
        return min

    def getMinY(self):
        min = 100000
        for items in self.geo:
            for x in items:
                for z in x:
                    if (type(z) is float):
                        if (z < min):
                            min = z
                    else:
                        if (z[1] < min):
                            min = z[1]
        return min

    def getGeometry(self, geo):
        dict = {}
        for index, item in enumerate(geo['coordinates']):
            dict[str(index)] = item
        return geo['coordinates']

    def prn(self):
        if (self.geo != None):
            print(self.geo)

    def writejson(self, filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def getCountryBoundaries(self):
        if (self.countryName == None):
            return (None, "Invalid country name.")
        if (not os.path.isfile(self.dataFile)):
            return (None, "Invalid file path.")
        with open(self.dataFile) as json_file:
            data = json.load(json_file)

            p = data['features']
            type = data['type']
            if (type != "FeatureCollection"):
                return (None, "Invalid format file")
            print(self.countryName)
            cName, cISO, cGeometry = self.getCountryByName(p, self.countryName)
            self.geo = self.getGeometry(cGeometry)
            self.minX = self.getMinX()
            self.minY = self.getMinY()
            return self.geo
            # for idx, point in enumerate(g):
            #    c = point
            #    print('index:%d %f %f ' % (idx, c[0], c[1]))

    # def createBoundaries(self):
    #     line = hou.node('/obj').createNode('geo').createNode('line')
    #     g = line.geometry()
    #     for item in self.geo:
    #         for i in item:
    #             for z in i:
    #                 print z

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
    import geotest

    geo = geotest.GeoTest(geotest.CNTR_BN_01M_2016_3035)
    geo.process()
    boundaries = CountryBoundaries('countries.geojson', 'Aruba')
    print (boundaries)
    list = boundaries.getCountryBoundaries()
    countries = boundaries.getcountriesname()
    boundaries.writejson("d:/temp/countries.json", countries)
    countries = boundaries.getcountriesnamefromfile("d:/temp/countries.json")
    cc = []
    for con in countries:
        cc.append(con['name'])
        cc.append(con['name'])
    # mENU
    attribs = [a for a in [2, 1, 3]]

    # l = chain(*zip(attribs, attribs))
    # Menu
    country = []
    # list = boundaries.getcountriesname()

    x = boundaries.getMinX()
    y = boundaries.getMinY()
    # boundaries.prn()
    for x in list:
        # poly = geo.createPolygon()
        for y in x:
            for z in y:
                # pt = geo.createPoint()
                # pt.setPosition(hou.Vector3(z.x, z.y, z.z))
                if (type(z) is float):
                    break
                print z[1]
    # boundaries.createBoundaries()

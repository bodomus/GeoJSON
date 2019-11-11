### Learn python types
###
# from datapackage import Package
import os
import json


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

    def print(self):
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

boundaries = CountryBoundaries('countries.geojson', 'Ukraine')
boundaries.getCountryBoundaries()
boundaries.print()
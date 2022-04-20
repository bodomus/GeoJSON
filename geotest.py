### Learn python types
###
# from datapackage import Package
import os
import json

# import hou


CNTR_BN_01M_2016_3035 = r'd:\Work\GeoData\JSON\CNTR_BN_01M_2016_3035.json'


class GeoTest:
    def __init__(self, datafile):
        if not os.path.isfile(datafile):
            raise Exception("The error occurred. File does not exist. ")
        if not isinstance(datafile, str):
            raise ValueError('Inappropriate type: {} for datafile whereas a str \
                   is expected'.format(type(datafile)))
        self.dataFile = datafile
        self.geo = None
        self.objects = None
        self.type = None
        self.transform = None
        self.arcs = None
        self.geometryCollection = None

    def process(self):
        with open(self.dataFile) as json_file:
            data = json.load(json_file)
            self.objects = data['objects']

            self.type = data['type']
            self.arcs = data['arcs']
            self.processarcs(self.arcs)
            self.transform = data['transform']
            n = self.getgeometrycollection()
            self.geometryCollection = self.objects[n]

            # type = data['type']
            # if (type != "FeatureCollection"):
            # return (None, "Invalid format file")

    def getgeometrycollection(self):
        n = self.dataFile
        return os.path.splitext(os.path.basename(n))[0]

    def processarcs(self, arcs):
        for l1 in arcs:
            for l2 in l1:
                print(l2[0], l2[1])
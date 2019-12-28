### Learn python types
###
# from datapackage import Package
import os
import json
#import hou


CNTR_BN_01M_2016_3035 = r'd:\Work\GeoData\GeoJSON\CNTR_BN_01M_2016_3035.json'

class geotest():
    def __init__(self, dataFile):
        if (not os.path.isfile(dataFile)):
            raise Exception("The error occured. File does not exist. ")
        self.dataFile = dataFile
        self.geo = None
        self.objects = None
        self.type =  None
        self.geometryCollection =  None

    def process(self):
        with open(self.dataFile) as json_file:
            data = json.load(json_file)
            self.objects = data['objects']
            self.type =  data['type']
            str =  self.getGeometryCollection()
            self.geometryCollection  =  self.objects[str]

            print(self.country)

            # type = data['type']
            #if (type != "FeatureCollection"):
                #return (None, "Invalid format file")

    def getGeometryCollection(self):
        str =  self.dataFile
        return os.path.splitext(os.path.basename(str))[0]



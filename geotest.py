### Learn python types
###
# from datapackage import Package
import os
import json

# import hou
CNTR_BN_01M_2016_3035 = r'd:\Work\GeoData\GeoJSON\CNTR_BN_01M_2016_3035.json'

class Geotest():
    def __init__(self, dataFile):
        self.country = None
        if not os.path.isfile(dataFile):
            raise Exception("The error occurred. File does not exist. ")
        self.data_file = dataFile
        self.geo = None
        self.objects = None
        self.type = None
        self.geometryCollection = None

    def process(self):
        with open(self.data_file) as json_file:
            data = json.load(json_file)
            self.objects = data['objects']
            self.type = data['type']
            str = self.get_geometry_collection()
            self.geometryCollection = self.objects[str]

            print(self.country)

            # type = data['type']
            # if (type != "FeatureCollection"):
            # return (None, "Invalid format file")

    def get_geometry_collection(self):
        str = self.data_file
        return os.path.splitext(os.path.basename(str))[0]

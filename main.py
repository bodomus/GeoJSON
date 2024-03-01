### Learn python types
###
# from datapackage import Package
import os
import json
# from geotest import Geotest
from functools import partial
# from geotest import CNTR_BN_01M_2016_3035


# import hou


def get_country_by_name(items, name):
    for item in items:
        i = item['properties']
        if (i['ADMIN'] == name):
            return (i['ADMIN'], i['ISO_A3'], item['geometry'])
    return None


class CountryBoundaries():

    def __init__(self, data_file, country_name):
        self.minY = None
        self.minX = None
        if not os.path.isfile(data_file):
            raise hou.NodeError("The error occured. File does not exist. ")
        self.data_file = data_file
        self.country_name = country_name
        self.geo = None
        self.use_different_height_for_groups = True

    # add in version 1.0.4
    def set_different_height_flag(self, is_use):
        self.use_different_height_for_groups = is_use

    def set_country_name(self, short_name):
        if short_name is not None:
            c_name, c_iso, c_geometry = self.get_country_by_short_name(short_name)
            self.country_name = c_name

    # add in version 1.0.4
    def get_different_height_flag(self):
        return self.use_different_height_for_groups

    def get_country(self):
        return self.country_name

    def get_version(self):
        return 'ver 1.0.5'

    def get_countries_name_from_file(self, filename):
        if not os.path.isfile(filename):
            return None, "Invalid file path."
        with open(filename) as json_file:
            data = json.load(json_file)
        return data

    def get_countries_name(self):
        if not os.path.isfile(self.data_file):
            return None, "Invalid file path."
        with open(self.data_file) as json_file:
            data = json.load(json_file)

            p = data['features']
            type = data['type']
            if type != "FeatureCollection":
                return None, "Invalid format file"
        list = []
        for item in p:
            i = item['properties']
            list.append({'name': i['ADMIN'], 'shortname': i['ISO_A3']})

        return list

    def get_country_by_short_name(self, items, shortname):
        for item in items:
            i = item['properties']
            if i['ISO_A3'] == shortname:
                return i['ADMIN'], i['ISO_A3'], item['geometry']
        return None

    def get_min_x(self):
        min = 100000
        for items in self.geo:
            for x in items:
                for z in x:
                    if type(z) is float:
                        if z < min:
                            min = z
                    else:
                        if z[0] < min:
                            min = z[0]
        return min

    def get_min_y(self):
        min = 100000
        for items in self.geo:
            for x in items:
                for z in x:
                    if type(z) is float:
                        if z < min:
                            min = z
                    else:
                        if z[1] < min:
                            min = z[1]
        return min

    def get_geometry(self, geo):
        dict = {}
        for index, item in enumerate(geo['coordinates']):
            dict[str(index)] = item
        return geo['coordinates']

    def write_json_to_file(self, filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def get_country_boundaries(self):
        if self.country_name is None:
            return None, "Invalid country name."
        if not os.path.isfile(self.data_file):
            return None, "Invalid file path."
        with open(self.data_file) as json_file:
            data = json.load(json_file)

            p = data['features']
            type = data['type']
            if type != "FeatureCollection":
                return None, "Invalid format file"
            c_name, c_iso, c_geometry = get_country_by_name(p, self.country_name)
            self.geo = self.get_geometry(c_geometry)
            self.minX = self.get_min_x()
            self.minY = self.get_min_y()
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


# with open(r'c:\Houdini\17.5.327\Readme.txt', 'rb') as handle:
#     read_block = partial(handle.read, 64)
#     for block in iter(read_block, ''):
#         print(block)


# def add(*args, **kwargs):
#     print(kwargs)


# l = [1, 2, 3, 4]
# add(l, 1, 2, 3, 4)

if __name__ == "__main__":
    import os
    import hou
    import json
    import hrpyc
    # import geotest

    # geo = Geotest(CNTR_BN_01M_2016_3035)
    # geo.process()
    boundaries = CountryBoundaries('countries.geojson', 'Aruba')
    print(boundaries)
    list = boundaries.get_country_boundaries()
    countries = boundaries.get_countries_name()
    boundaries.write_json_to_file("d:/temp/countries.json", countries)
    countries = boundaries.get_countries_name_from_file("d:/temp/countries.json")
    cc = []
    for con in countries:
        cc.append(con['name'])
        cc.append(con['name'])
    # mENU
    attribs = [a for a in [1, 2, 3]]

    # l = chain(*zip(attribs, attribs))
    # Menu
    country = []
    # list = boundaries.getcountriesname()

    x = boundaries.get_min_x()
    y = boundaries.get_min_y()
    # boundaries.prn()
    # for x in list:
    #     #poly = geo.createPolygon()
    #     for y in x:
    #         for z in y:
    #             #pt = geo.createPoint()
    #             #pt.setPosition(hou.Vector3(z.x, z.y, z.z))
    #             if  (type(z) is float):
    #                 break
    #             print z[1]
    # boundaries.createBoundaries()

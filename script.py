from xml.dom import minidom
import csv
 
class ParseSVG():
   
    def __init__(self, svg_name, csv_name):
        #self.svg_name = input('SVG File: ')
        #self.csv_name = input('CSV File: ')
 
        self.svg_name = svg_name
        self.csv_name = csv_name
 
    def getAttributes(self):
        coordinates = []
       
        mydoc = minidom.parse(self.svg_name)
        path_tag = mydoc.getElementsByTagName("image")
 
        i = 0
        for d_string in path_tag:
            name = path_tag[i].attributes['id'].value
            w = path_tag[i].attributes['width'].value
            h = path_tag[i].attributes['height'].value
            temp_transform = path_tag[i].attributes['transform'].value
 
            transform = temp_transform.split(' ', 5)
           
            temp = [
                name,
                round(float(w)),
                round(float(h)),
                round(float(transform[4])),
                round(float(transform[5][:-1]))
            ]
 
            coordinates.append(temp)
           
            i = i + 1
 
        return coordinates
 
    def createFile(self):
        header = ['Name', 'W', 'H', 'X', 'Y']
        with open(self.csv_name, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(self.getAttributes())
 
        print('%s successful created!' % self.csv_name)
 
f = ParseSVG('b.svg', 'b.csv')
f.createFile()

from xml.dom import minidom
import csv
 
class ParseSVG():
   
    def __init__(self, svg_name, csv_name):
    
      # User can submit file names #
        #self.svg_name = input('SVG File (name.svg): ')
        #self.csv_name = input('CSV File (name.csv): ')
 
        self.svg_name = svg_name
        self.csv_name = csv_name
 
    def getAttributes(self):
        coordinates = []
       
        mydoc = minidom.parse(self.svg_name)
        path_tag = mydoc.getElementsByTagName("image") # Get image tag from svg
 
        i = 0
        for d_string in path_tag:
            name = path_tag[i].attributes['id'].value # Get id (layer name in Illustrator) from image
            w = path_tag[i].attributes['width'].value
            h = path_tag[i].attributes['height'].value
            temp_transform = path_tag[i].attributes['transform'].value # Get position and rotation from image
 
            transform = temp_transform.split(' ', 5) # I need only last 2 value. So I split the space ' '
           
            temp = [
                name,
                round(float(w)),
                round(float(h)),
                round(float(transform[4])), # Get fourth index from transform variable
                round(float(transform[5][:-1])) # Get fifth index from transform variable and delete last 2 character
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

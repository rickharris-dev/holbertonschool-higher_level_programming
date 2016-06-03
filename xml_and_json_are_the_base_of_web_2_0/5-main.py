from car import Car
from xml.dom.minidom import Document
import json

cars = []
brands = []
doors = 0
doc = Document()

'''Loads the json data from the file'''
json_file = open("5-main.json")
data = json.loads(json_file.read())

'''Initializes a XML document'''
xml_cars = doc.createElement('cars')
doc.appendChild(xml_cars)

'''Creates a list of car classes from JSON data'''
for car in data:
    car = Car(car)
    cars.append(car)

for car in cars:

    '''Creates a list of unique brands'''
    brand = car.get_brand()
    if not brand in brands:
        brands.append(brand)

    '''Calculates a total of doors on all cars'''
    doors += car.get_nb_doors()

    '''Adds the car to the XML document'''
    c_xml = car.to_xml_node(doc)
    xml_cars.appendChild(c_xml)

'''Prints the number of brands, door count, the 4th car, and the XML doc'''
print len(brands)
print doors
print cars[3]
print doc.toxml(encoding='utf-8')

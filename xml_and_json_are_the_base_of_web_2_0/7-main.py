# -*- coding: utf-8

from car import Car
from xml.dom.minidom import Document
import json
import sys

'''Allows UTF-8 characters'''
reload(sys)
sys.setdefaultencoding('utf8')

cars = []
doc = Document()

'''Loads json data from file'''
json_file = open("7-main.json")
data = json.loads(json_file.read())

'''Initializes the xml document'''
xml_cars = doc.createElement('cars')
doc.appendChild(xml_cars)

'''Creates a list of Car classes'''
for car in data:
    car = Car(car)
    cars.append(car)

for car in cars:
    '''Converts car to xml node'''
    c_xml = car.to_xml_node(doc)

    '''Add year element to the car'''
    year = doc.createElement('year')
    year_content = doc.createTextNode('2015')
    year.appendChild(year_content)
    c_xml.appendChild(year)

    '''Sets the weight attribute of the car'''
    c_xml.setAttribute('weight', '1000')

    '''Converts the brand element to a CDATA section with the © symbol added'''
    brand = c_xml.getElementsByTagName('brand')[0]
    new_brand = '©' + brand.childNodes[0].nodeValue
    brand_content = doc.createCDATASection(new_brand)
    brand.removeChild(brand.childNodes[0])
    brand.appendChild(brand_content)

    '''Adds the car node to the XML doc'''
    xml_cars.appendChild(c_xml)

'''Prints the XML doc'''
print doc.toxml(encoding='utf-8')

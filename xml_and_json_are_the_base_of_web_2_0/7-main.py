# -*- coding: utf-8

from car import Car
from xml.dom.minidom import Document
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

cars = []
doc = Document()

json_file = open("7-main.json")
data = json.loads(json_file.read())
xml_cars = doc.createElement('cars')
doc.appendChild(xml_cars)

for car in data:
    car = Car(car)
    cars.append(car)

for car in cars:
    c_xml = car.to_xml_node(doc)

    year = doc.createElement('year')
    year_content = doc.createTextNode('2015')
    year.appendChild(year_content)
    c_xml.appendChild(year)

    c_xml.setAttribute('weight', '1000')

    brand = c_xml.getElementsByTagName('brand')[0]
    new_brand = '©' + brand.childNodes[0].nodeValue
    brand_content = doc.createCDATASection(new_brand)
    brand.removeChild(brand.childNodes[0])
    brand.appendChild(brand_content)

    xml_cars.appendChild(c_xml)

print doc.toxml(encoding='utf-8')

from car import Car
from xml.dom.minidom import Document
import json

cars = []
brands = []
doors = 0
doc = Document()

json_file = open("5-main.json")
data = json.loads(json_file.read())
xml_cars = doc.createElement('cars')
doc.appendChild(xml_cars)

for car in data:
    car = Car(car)
    cars.append(car)

for car in cars:
    brand = car.get_brand()
    if not brand in brands:
        brands.append(brand)
    doors += car.get_nb_doors()
    c_xml = car.to_xml_node(doc)
    xml_cars.appendChild(c_xml)

print len(brands)
print doors
print cars[3]
print doc.toxml(encoding='utf-8')

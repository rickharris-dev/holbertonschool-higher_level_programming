from xml.dom.minidom import Document
from car import Car

c = Car(name="Rogue", brand="Nissan", nb_doors=5)
print c
c_json_string = c.to_json_string()
print type(c_json_string)
print c_json_string

doc = Document()
c_xml = c.to_xml_node(doc)
doc.appendChild(c_xml)
print doc.toxml(encoding='utf-8')

import json

class Car:

    def __init__(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, dict):
                    if 'name' in arg:
                        name = str(arg.pop('name'))
                    if 'brand' in arg:
                        brand = str(arg.pop('brand'))
                    if 'nb_doors' in arg:
                        nb_doors = arg.pop('nb_doors')
                if isinstance(arg, str) and len(arg.split(',')) == 3:
                    values = arg.split(',')
                    name = values[0]
                    brand = values[1]
                    nb_doors = int(values[2])

        if 'name' in kwargs:
            name = kwargs.pop('name')
        if 'brand' in kwargs:
            brand = kwargs.pop('brand')
        if 'nb_doors' in kwargs:
            nb_doors = kwargs.pop('nb_doors')

        if name == None or not isinstance(name, str) or name == "":
            raise Exception("name is not a string")
        elif brand == None or not isinstance(brand, str) or brand == "":
            raise Exception("brand is not a string")
        elif nb_doors == None or not isinstance(nb_doors, int) or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_nb_doors(self):
        return self.__nb_doors

    def to_hash(self):
        return  {
            'nb_doors': self.__nb_doors,
            'brand': self.__brand,
            'name': self.__name
        }

    def set_nb_doors(self, number):
        self.__nb_doors = number

    def __str__(self):
        return self.__brand + " " + self.__name + " (" + str(self.__nb_doors) + ")"

    def to_json_string(self):
        return json.dumps(self.to_hash())

    def to_xml_node(self, doc):
        car = doc.createElement('car')
        car.setAttribute('nb_doors', str(self.__nb_doors))

        name = doc.createElement('name')
        name_content = doc.createCDATASection(self.__name)
        name.appendChild(name_content)
        car.appendChild(name)

        brand = doc.createElement('brand')
        brand_content = doc.createTextNode(self.__brand)
        brand.appendChild(brand_content)
        car.appendChild(brand)

        return car

    def to_comma(self):
        return self.__name + "," + self.__brand + "," + str(self.__nb_doors) + "\n"

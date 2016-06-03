from car import Car
import json

cars = []
comma_cars = []

'''Loads json data from file'''
json_file = open("6-main.json")
data = json.loads(json_file.read())

'''Creates a list of comma-separated car values'''
for car in data:
    car = Car(car)
    cars.append(car)
    comma_cars.append(car.to_comma())

'''Prints the list of cars'''
print "".join(comma_cars)

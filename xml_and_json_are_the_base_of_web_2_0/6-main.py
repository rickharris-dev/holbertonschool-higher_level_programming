from car import Car
import json

cars = []
comma_cars = []

json_file = open("6-main.json")
data = json.loads(json_file.read())

for car in data:
    car = Car(car)
    cars.append(car)
    comma_cars.append(car.to_comma())

print "".join(comma_cars)

''' Defines a Circle class with the listed attributes and methods '''

import math

class Circle():

    def __init__(self, radius):
        ''' Initializes a circle with a defined radius. '''
        self.radius = radius

    def __delete__(self):
        ''' Deletes the circle '''
        pass

    def set_center(self, array):
        ''' Sets the center of the circle at [x, y] coordinates '''
        self.__center = array

    def get_center(self):
        ''' Returns the center of the [x, y] coordinates of the circle '''
        return self.__center

    def set_color(self, color):
        ''' Sets the color of the circle '''
        self.__color = color

    def get_color(self):
        ''' Returns the color of the circle '''
        return self.__color

    def area(self):
        ''' Returns the area of the circle '''
        return (self.radius ** 2) * math.pi

    def intersection(self, c_bis):
        ''' Determines if the circles intersect or overlap and returns True or False '''
        a = self.__center
        b = c_bis.get_center()
        dist = math.sqrt((abs(a[0] - b[0]) ** 2) + (abs(a[1] - b[1]) ** 2))
        if dist <= self.radius + c_bis.radius:
            return True
        return False

    def intersection_percentage(self, c_bis):
        ''' Returns the percentage that two circles intersect or overlap '''
        a = self.__center
        b = c_bis.get_center()
        dist = math.sqrt((abs(a[0] - b[0]) ** 2) + (abs(a[1] - b[1]) ** 2))
        s = (dist + self.radius + c_bis.radius) / 2
        chord = 2 * ((2 * math.sqrt(s * (s - dist) * (s - self.radius) * (s - c_bis.radius))) / dist)
        angle_a = math.asin((chord / 2) / self.radius) * 2
        segment_a = self.area() * (angle_a / (2 * math.pi))
        triangle_a = (chord * math.sqrt((self.radius ** 2) - ((chord / 2) ** 2))) / 2
        angle_b = math.asin((chord / 2) / c_bis.radius) * 2
        segment_b = c_bis.area() * (angle_b / (2 * math.pi))
        triangle_b = (chord * math.sqrt((c_bis.radius ** 2) - ((chord / 2) ** 2))) / 2
        return ((segment_a - triangle_a) + (segment_b - triangle_b)) / self.area() * 100

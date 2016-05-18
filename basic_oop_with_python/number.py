''' Defines the Number class with the listed attributes and methods '''
class Number():

    def __init__(self, value):
        ''' Initiates the number with the given value '''
        self.__value = value

    def __del__(self):
        ''' Deletes the number '''
        pass

    def __str__(self):
        ''' Returns the value as a string when called '''
        return str(self.__value)

    def __add__(self, other):
        ''' Defines the addition operator '''
        return self.get_value() + other.get_value()

    def __sub__(self, other):
        ''' Defines the subtraction operator '''
        return self.get_value() - other.get_value()

    def __mul__(self, other):
        ''' Defines the multiplication operator '''
        return self.get_value() * other.get_value()

    def __div__(self, other):
        ''' Defines the division operator '''
        return self.get_value() / other.get_value()

    def set_value(self, value):
        ''' Sets the value '''
        self.__value = value

    def get_value(self):
        ''' Returns the value '''
        return self.__value
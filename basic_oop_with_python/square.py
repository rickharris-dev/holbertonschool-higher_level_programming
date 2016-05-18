''' Defines a Square() with the listed public and private attributes and methods '''
class Square():

    def __init__(self, side_length):
        ''' Initializes the square and the __side_length and name attributes '''
        self.__side_length = side_length
        self.name = ''

    def __del__(self):
        ''' Deletes the square '''
        pass

    def __str__(self):
        ''' Returns the layout of the square to be printed '''
        if self.__side_length <= 0:
            return ''
        elif self.__side_length == 1:
            return '*'
        else:
            i = 2;
            square = ''
            square += self.__print_top_or_bottom() + '\n'
            while i < self.__side_length:
                square += self.__print_middle() + '\n'
                i += 1
            square += self.__print_top_or_bottom()
            return square

    def __print_top_or_bottom(self):
        ''' Creates the top & bottom lines of the square to be printed '''
        i = 0;
        line = ''
        while i < self.__side_length:
            line += '*'
            i += 1
        return line

    def __print_middle(self):
        ''' Creates the middle lines of the square to be printed '''
        i = 0;
        line = ''
        while i < self.__side_length:
            if i == 0 or i == self.__side_length - 1:
                line += '*'
            else:
                line += ' '
            i += 1
        return line

    def set_center(self, array):
        ''' Sets the center of the square at [x, y] coordinates '''
        self.__center = array

    def get_center(self):
        ''' Returns the center of the [x, y] coordinates of the square '''
        return self.__center

    def set_color(self, color):
        ''' Sets the color of the square '''
        self.__color = color

    def get_color(self):
        ''' Returns the color of the square '''
        return self.__color

    def area(self):
        ''' Calculates and returns the area of the square '''
        return self.__side_length ** 2
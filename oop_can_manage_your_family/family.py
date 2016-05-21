class Person():

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        self.EYES_COLORS = ["Blue", "Green", "Brown"]
        self.GENRES = ["Female", "Male"]

        try:
            self.__id(id)
        except:
            raise Exception("id is not an integer")

        try:
            self.__first_name(first_name)
        except:
            raise Exception("first_name is not a string")

        try:
            self.__date_of_birth(date_of_birth)
        except:
            raise Exception("date_of_birth is not a valid date")

        try:
            self.__genre(genre)
        except:
            raise Exception("genre is not valid")

        try:
            self.__eyes_color(eyes_color)
        except:
            raise Exception("eyes_color is not valid")

        self.last_name = None


    def __del__(self):
        pass

    def __str__(self):
        return self.__first_name + ' ' + self.last_name

    def __lt__(self, other):
        return self.age() < other.age()

    def __le__(self, other):
        return self.age() <= other.age()

    def __eq__(self, other):
        return self.age() == other.age()

    def __ge__(self, other):
        return self.age() >= other.age()

    def __gt__(self, other):
        return self.age() > other.age()

    def __id(self, value):
        if not isinstance(value, int):
            raise
        elif value < 0:
            raise
        else:
            self.__id = value

    def __first_name(self, value):
        if not isinstance(value, str):
            raise
        elif value == '':
            raise
        else:
            self.__first_name = value

    def __date_of_birth(self, value):
        if not len(value) == 3:
            print "Error 1"
            raise
        elif not all(isinstance(n, int) for n in value):
            print "Error 2"
            raise
        elif not 1 <= value[0] <= 12:
            print "Error 3"
            raise
        elif not 1 <= value[1] <= 31:
            print "Error 4"
            raise
        else:
            self.__date_of_birth = value

    def __genre(self, value):
        if not isinstance(value, str):
            raise
        elif not value in self.GENRES:
            raise
        else:
            self.__genre = value

    def __eyes_color(self, value):
            if not isinstance(value, str):
                raise
            elif not value in self.EYES_COLORS:
                raise
            else:
                self.__eyes_color = value

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_genre(self):
        return self.__genre

    def get_eyes_color(self):
        return self.__eyes_color

    def is_male(self):
        return self.__genre == 'Male'

    def age(self):
        date = [5, 20, 2016]
        if self.__date_of_birth[0] > date[0]:
            return date[2] - self.__date_of_birth[2] - 1
        elif self.__date_of_birth[0] == date[0] and self.__date_of_birth[1] > date[1]:
            return date[2] - self.__date_of_birth[2] - 1
        else:
            return date[2] - self.__date_of_birth[2]

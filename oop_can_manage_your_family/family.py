import json

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
        self.is_married_to = 0
        self.children = []


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

    def json(self):
        '''returns hash with id, eyes_color, genre, date_of_birth, first_name, last_name'''
        json = {
            'id': self.__id,
            'eyes_color': self.__eyes_color,
            'genre': self.__genre,
            'date_of_birth': self.__date_of_birth,
            'first_name': self.__first_name,
            'last_name': self.last_name,
            'is_married_to': self.is_married_to
        }
        return json

    def load_from_json(self, json):
        if not isinstance(json, dict):
            raise Exception("json is not valid")
        else:
            self.__id = json['id']
            self.__first_name = json['first_name']
            self.__date_of_birth = json['date_of_birth']
            self.__genre = json['genre']
            self.__eyes_color = json['eyes_color']
            self.last_name = json['last_name']
            self.is_married_to = json['is_married_to']

class Baby(Person):

    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        return False

    def divorce(self, p):
        raise Exception("Not currently married")

    def just_married_with(self, p):
        raise Exception("Can't be married")

    def can_have_child(self):
        return False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        raise Exception("Can't have a child")

    def adopt_child(self, c):
        raise Exception("Can't adopt a person")

class Teenager(Person):

    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        return False

    def divorce(self, p):
        raise Exception("Not currently married.")

    def just_married_with(self, p):
        raise Exception("Can't be married")

    def can_have_child(self):
        return False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        raise Exception("Can't have a child")

    def adopt_child(self, c):
        raise Exception("Can't adopt a person")

class Adult(Person):

    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        if self.is_married_to != 0:
            return True
        return False

    def divorce(self, p):
        if self.is_married_to == p.id and self.id == p.is_married_to:
            self.is_married_to = 0
            p.is_married_to = 0
        else:
            raise Exception("Couple is not currently married.")

    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        elif p.can_be_married() == False:
            raise Exception("Can't be married")
        else:
            self.is_married_to = p.get_id()
            p.is_married_to = self.get_id()
            if p.get_genre() == 'Male':
                self.last_name = p.last_name

    def can_have_child(self):
        return True

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if p.can_have_child() == False or p is None:
            raise Exception("Can't have a child")
        elif not isinstance(id, int) or id < 0:
            raise Exception("id is not an integer")
        elif not isinstance(first_name, str) or first_name == '':
            raise Exception("string is not a string")
        elif not all(isinstance(n, int) for n in date_of_birth) or len(date_of_birth) != 3:
            raise Exception("date_of_birth is not a valid date")
        elif not isinstance(genre, str) or not genre in self.GENRES:
            raise Exception("genre is not valid")
        elif not isinstance(eyes_color, str) or not eyes_color in self.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        else:
            baby = Baby(id, first_name, date_of_birth, genre, eyes_color)
            p.children.append(baby.get_id())
            self.children.append(baby.get_id())

    def adopt_child(self, c):
        if c.__class__.__name__ != 'Baby' and c.__class__.__name__ != 'Teenager':
            raise Exception("c can't be adopted")
        else:
            self.children.append(c.get_id())

class Senior(Person):

    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        if self.is_married_to != 0:
            return True
        return False

    def divorce(self, p):
        if self.is_married_to == p.id and self.id == p.is_married_to:
            self.is_married_to = 0
            p.is_married_to = 0
        else:
            raise Exception("Couple is not currently married.")

    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        elif p.can_be_married() == False:
            raise Exception("Can't be married")
        else:
            self.is_married_to = p.get_id()
            p.is_married_to = self.get_id()
            if p.get_genre() == 'Male':
                self.last_name = p.last_name

    def can_have_child(self):
        return False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        raise Exception("Can't have a child")

    def adopt_child(self, c):
        raise Exception("Can't adopt a person")

def save_to_file(list, filename):
    output = []
    for person in list:
        data = person.json()
        data['type'] = person.__class__.__name__
        output.append(data)
    f = open(filename, 'w')
    f.write(json.dumps(output))
    f.close()

def load_from_file(filename):
    f = open(filename, 'r')
    data = f.read()
    data = json.loads(data)
    family = list()
    d = [0, 'new', [1,1,1], 'Male', 'Brown']
    for person in data:
        if person['type'] == 'Baby':
            new = Baby(d[0], d[1], d[2], d[3], d[4])
        elif person['type'] == 'Teenager':
            new = Teenager(d[0], d[1], d[2], d[3], d[4])
        elif person['type'] == 'Adult':
            new = Adult(d[0], d[1], d[2], d[3], d[4])
        elif person['type'] == 'Senior':
            new = Senior(d[0], d[1], d[2], d[3], d[4])
        new.load_from_json(person)
        family.append(new)
    f.close()
    return family

import json

class Person():
    '''Defines a Person class'''

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        '''Initializes a Person class object'''

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
        '''Deletes the given object'''
        pass

    def __str__(self):
        '''Returns string providing first and last name if last is known'''
        if self.last_name:
            return self.__first_name + ' ' + self.last_name
        return self.__first_name

    def __lt__(self, other):
        '''Compares if self is younger than other'''
        return self.age() < other.age()

    def __le__(self, other):
        '''Compares if self is younger or the same age as other'''
        return self.age() <= other.age()

    def __eq__(self, other):
        '''Compares if self is the same age as other'''
        return self.age() == other.age()

    def __ge__(self, other):
        '''Compares if self is older or the same age as other'''
        return self.age() >= other.age()

    def __gt__(self, other):
        '''Compares if self is older than other'''
        return self.age() > other.age()

    def __id(self, value):
        '''Sets __id attribute if value is valid'''
        if not isinstance(value, int):
            raise
        elif value < 0:
            raise
        else:
            self.__id = value

    def __first_name(self, value):
        '''Sets __first_name attribute if value is valid'''
        if not isinstance(value, str):
            raise
        elif value == '':
            raise
        else:
            self.__first_name = value

    def __date_of_birth(self, value):
        '''Sets __date_of_birth attribute if value is valid'''
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
        '''Sets __genre attribute if value is valid'''
        if not isinstance(value, str):
            raise
        elif not value in self.GENRES:
            raise
        else:
            self.__genre = value

    def __eyes_color(self, value):
        '''Sets __eyes_color attribute if value is valid'''
            if not isinstance(value, str):
                raise
            elif not value in self.EYES_COLORS:
                raise
            else:
                self.__eyes_color = value

    def get_id(self):
        '''Returns the __id attribute for the Person'''
        return self.__id

    def get_first_name(self):
        '''Returns the __first_name attribute for the Person'''
        return self.__first_name

    def get_date_of_birth(self):
        '''Returns the __date_of_birth attribute for the Person'''
        return self.__date_of_birth

    def get_genre(self):
        '''Returns the __genre attribute for the Person'''
        return self.__genre

    def get_eyes_color(self):
        '''Returns the __eyes_color attribute for the Person'''
        return self.__eyes_color

    def is_male(self):
        '''Returns the True if the Person is male'''
        return self.__genre == 'Male'

    def age(self):
        '''Returns age of Person based on date of 5/20/2016'''
        date = [5, 20, 2016]
        if self.__date_of_birth[0] > date[0]:
            return date[2] - self.__date_of_birth[2] - 1
        elif self.__date_of_birth[0] == date[0] and self.__date_of_birth[1] > date[1]:
            return date[2] - self.__date_of_birth[2] - 1
        else:
            return date[2] - self.__date_of_birth[2]

    def json(self):
        '''Returns hash with id, eyes_color, genre, date_of_birth, first_name, last_name'''
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
        '''Sets Person attributes based on loaded json data'''
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
    '''Defines a Baby class that inherits from the Person class'''

    def can_run(self):
        '''Defines that a Baby cannot run'''
        return False

    def need_help(self):
        '''Defines that a Baby needs help'''
        return True

    def is_young(self):
        '''Defines that a Baby is young in age'''
        return True

    def can_vote(self):
        '''Defines that a Baby cannot vote'''
        return False

    def can_be_married(self):
        '''Defines that a Baby cannot be married'''
        return False

    def is_married(self):
        '''Defines that a Baby is not married'''
        return False

    def divorce(self, p):
        '''Defines that a Baby cannot divorce'''
        raise Exception("Not currently married")

    def just_married_with(self, p):
        '''Defines that a Baby cannot be married'''
        raise Exception("Can't be married")

    def can_have_child(self):
        '''Defines that a Baby cannot have a child'''
        return False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        '''Defines that a Baby cannot have a child'''
        raise Exception("Can't have a child")

    def adopt_child(self, c):
        '''Defines that  Baby cannot adopt a person'''
        raise Exception("Can't adopt a person")

class Teenager(Person):
    '''Defines a Teenager class that inherits from the Person class'''

    def can_run(self):
        '''Defines that a Teenager can run'''
        return True

    def need_help(self):
        '''Defines that a Teenager does not need help'''
        return False

    def is_young(self):
        '''Defines that a Teenager is young'''
        return True

    def can_vote(self):
        '''Defines that a Teenager cannot vote'''
        return False

    def can_be_married(self):
        '''Defines that a Teenager cannot be married'''
        return False

    def is_married(self):
        '''Defines that a Teenager is not married'''
        return False

    def divorce(self, p):
        '''Defines that a Teenager cannot divorce'''
        raise Exception("Not currently married.")

    def just_married_with(self, p):
        '''Defines that a Teenager cannot be married'''
        raise Exception("Can't be married")

    def can_have_child(self):
        '''Defines that a Teenager cannot have a child'''
        return False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        '''Defines that a Teenager cannot have a child'''
        raise Exception("Can't have a child")

    def adopt_child(self, c):
        '''Defines that a Teenager cannot adopt a person'''
        raise Exception("Can't adopt a person")

class Adult(Person):
    '''Defines an Adult class that inherits from the Person class'''

    def can_run(self):
        '''Defines that an Adult can run'''
        return True

    def need_help(self):
        '''Defines that an Adult does not need help'''
        return False

    def is_young(self):
        '''Defines that an Adult is not young'''
        return False

    def can_vote(self):
        '''Defines that an Adult can vote'''
        return True

    def can_be_married(self):
        '''Defines that an Adult can be married'''
        return True

    def is_married(self):
        '''Returns True if an Adult is married'''
        if self.is_married_to != 0:
            return True
        return False

    def divorce(self, p):
        '''Divorces two individuals if they are married'''
        if self.is_married_to == p.id and self.id == p.is_married_to:
            self.is_married_to = 0
            p.is_married_to = 0
        else:
            raise Exception("Couple is not currently married.")

    def just_married_with(self, p):
        '''Updates individuals to reflect marriage to one another'''
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
        '''Defines that an Adult can have a child'''
        return True

    def has_child_with(self, p, id, first_name, date_of_birth, genre, *eyes_color):
        '''Creates a new Baby and links the child to parents'''
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
        elif eyes_color and (not isinstance(eyes_color, str) or not eyes_color in self.EYES_COLORS):
            raise Exception("eyes_color is not valid")
        else:
            if not eyes_color:
                if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue':
                    eyes_color = 'Blue'
                elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green':
                    eyes_color = 'Green'
                elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Brown':
                    eyes_color = 'Brown'
                elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green':
                    eyes_color = 'Blue'
                elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Brown':
                    eyes_color = 'Brown'
                elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Brown':
                    eyes_color = 'Brown'
            baby = Baby(id, first_name, date_of_birth, genre, eyes_color)
            p.children.append(baby.get_id())
            self.children.append(baby.get_id())
            return baby

    def adopt_child(self, c):
        '''Links Person to Adult if the Person can be adopted'''
        if c.__class__.__name__ != 'Baby' and c.__class__.__name__ != 'Teenager':
            raise Exception("c can't be adopted")
        else:
            self.children.append(c.get_id())

class Senior(Person):
    '''Defines a Senior class that inherits from the Person class'''

    def can_run(self):
        '''Defines that a Senior cannot run'''
        return False

    def need_help(self):
        '''Defines that a Senior needs help'''
        return True

    def is_young(self):
        '''Defines that a Senior is not young'''
        return False

    def can_vote(self):
        '''Defines that a Senior can vote'''
        return True

    def can_be_married(self):
        '''Defines that a Senior can be married'''
        return True

    def is_married(self):
        '''Returns True if a Senior is married'''
        if self.is_married_to != 0:
            return True
        return False

    def divorce(self, p):
        '''Divorces a Senior and partner if currently married'''
        if self.is_married_to == p.id and self.id == p.is_married_to:
            self.is_married_to = 0
            p.is_married_to = 0
        else:
            raise Exception("Couple is not currently married.")

    def just_married_with(self, p):
        '''Updates Senior and partner to reflect marriage'''
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
        '''Defines that a Senior cannot have a child'''
        return False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        '''Defines that a Senior cannot have a child'''
        raise Exception("Can't have a child")

    def adopt_child(self, c):
        '''Defines that a Senior cannot adopt a person'''
        raise Exception("Can't adopt a person")

def save_to_file(list, filename):
    '''Saves a list of Persons to the given file in json format'''
    output = []
    for person in list:
        data = person.json()
        data['type'] = person.__class__.__name__
        output.append(data)
    f = open(filename, 'w')
    f.write(json.dumps(output))
    f.close()

def load_from_file(filename):
    '''Loads the saved Persons from the given file from json format'''
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

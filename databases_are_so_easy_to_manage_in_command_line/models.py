import peewee

''' Defines the chosen database and pragmas '''
my_models_db = peewee.SqliteDatabase('my_models.db', pragmas=(
    ('foreign_keys', 1),
))


class BaseModel(peewee.Model):
    ''' Defines the basic information required for all classes '''
    id = peewee.PrimaryKeyField(unique = True)

    class Meta:
        database = my_models_db
        order_by = ('id', )

class School(BaseModel):
    ''' Defines the School class and table '''
    name = peewee.FixedCharField(max_length = 128, null = False)

    def __str__(self):
        return "School: " + self.name + " (" + str(self.id) + ")"

class Batch(BaseModel):
    ''' Defines the Batch class and table and key relationship to school '''
    school = peewee.ForeignKeyField(rel_model = School, related_name = 'batches', on_delete = 'cascade')
    name = peewee.FixedCharField(max_length = 128, null = False)

    def __str__(self):
        return "Batch: " + self.name + " (" + str(self.id) + ")"

class User(BaseModel):
    ''' Defines the User class and table '''
    first_name = peewee.FixedCharField(max_length = 128, default = "")
    last_name = peewee.FixedCharField(max_length = 128, null = False)
    age = peewee.IntegerField(null = False)

    def __str__(self):
        return "User: " + self.first_name + " " + self.last_name + " (" + str(self.id) + ")"

class Student(User):
    ''' Defines the Student class and foreign key relationship to User '''
    batch = peewee.ForeignKeyField(rel_model = Batch, related_name = 'students', on_delete = 'cascade')

    def __str__(self):
        if self.first_name == "":
            name = self.last_name
        else:
            name = self.first_name + " " + self.last_name
        return "Student: " + name + " (" + str(self.id) + ") part of the batch: " + str(self.batch)

class Exercise(BaseModel):
    ''' Defines the Excercise class with foreign key relationship to Student '''
    SUBJECTS = [('math', "Math"), ('english', "English"), ('history', "History"), ('c_prog', "C prog"), ('swift_prog', "Swift prog")]
    student = peewee.ForeignKeyField(rel_model = Student, related_name = 'exercises', on_delete = 'cascade')
    subject = peewee.FixedCharField(max_length = 128, choices = SUBJECTS)
    note = peewee.IntegerField(default = 0)

    def __str__(self):
        return "Exercise: " + str(self.student) + " has " + str(self.note) + " in " + self.subject + " (" + str(self.id) + ")"

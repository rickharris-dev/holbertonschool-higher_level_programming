import peewee

my_models_db = peewee.SqliteDatabase('my_models.db', pragmas=(
    ('foreign_keys', 1),
))


class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique = True)

    class Meta:
        database = my_models_db
        order_by = ('id', )

class School(BaseModel):
    name = peewee.FixedCharField(max_length = 128, null = False)

    def __str__(self):
        return "School: " + self.name + " (" + str(self.id) + ")"

class Batch(BaseModel):
    school = peewee.ForeignKeyField(rel_model = School, related_name = 'batches', on_delete = 'cascade')
    name = peewee.FixedCharField(max_length = 128, null = False)

    def __str__(self):
        return "Batch: " + self.name + " (" + str(self.id) + ")"

class User(BaseModel):
    first_name = peewee.FixedCharField(max_length = 128, default = "")
    last_name = peewee.FixedCharField(max_length = 128, null = False)
    age = peewee.IntegerField(null = False)

    def __str__(self):
        return "User: " + self.first_name + " " + self.last_name + " (" + str(self.id) + ")"

class Student(User):
    batch = peewee.ForeignKeyField(rel_model = Batch, related_name = 'students', on_delete = 'cascade')

    def __str__(self):
        if self.first_name == "":
            name = self.last_name
        else:
            name = self.first_name + " " + self.last_name
        return "Student: " + name + " (" + str(self.id) + ") part of the batch: " + str(self.batch)

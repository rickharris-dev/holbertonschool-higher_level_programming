from peewee import *
from playhouse.fields import ManyToManyField

class BaseModel(Model):

    class Meta:
        order_by = ('id', )

class FilmModel(BaseModel):
    id = PrimaryKeyField(unique = True)
    title = FixedCharField(max_length = 128, null = False)
    release_date = FixedCharField(max_length = 128, null = False)
    episode_id = IntegerField(null = False)

class PeopleModel(BaseModel):
    id = PrimaryKeyField(unique = True)
    name = FixedCharField(max_length = 128, null = False)
    films = ManyToManyField(FilmModel, related_name='characters')

class PlanetModel(BaseModel):
    id = PrimaryKeyField(unique = True)
    name = FixedCharField(max_length = 128, null = False)
    climate = FixedCharField(max_length = 128, null = False)
    residents = ManyToManyField(PeopleModel, related_name='homeworld')
    films = ManyToManyField(FilmModel, related_name='planets')

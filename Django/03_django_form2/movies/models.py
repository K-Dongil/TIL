from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Movie(models.Model):
    title = CharField(max_length=100)
    overview = TextField()
    poster_path = CharField(max_length=500)
    
    def __str__(self):
        return self.title
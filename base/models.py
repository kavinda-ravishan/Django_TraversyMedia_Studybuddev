from django.db import models
from django.db.models.base import Model

class Room(models.Model):
    #host = 
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # database field (can Empty), form field (can Empty)
    #participants =
    updated = models.DateTimeField(auto_now=True) # everytime save (or updated) the field
    created = models.DateTimeField(auto_now_add=True) # first time created the field

    def __str__(self):
        return self.name

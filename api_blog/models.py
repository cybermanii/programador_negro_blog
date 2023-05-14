# import black
from django.db import models

class Types(models.Model):
    description = models.CharField(max_length=100, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(null=True)

class Movies(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey(Types, models.DO_NOTHING, related_name='movies' ) # serializer relationships
    power_level = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)

from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=80, unique=True)
    capacity = models.IntegerField()
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.name
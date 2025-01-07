from django.db import models

from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

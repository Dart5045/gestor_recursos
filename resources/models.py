from django.db import models

from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=100)  # Sin restricciones adicionales
    description = models.TextField()  # Sin limitación de longitud
    available = models.BooleanField(default=True)  # Sin restricciones adicionales

    def __str__(self):
        return self.name

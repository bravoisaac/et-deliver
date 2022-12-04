from django.db import models

# Create your models here.

class susario(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.rut
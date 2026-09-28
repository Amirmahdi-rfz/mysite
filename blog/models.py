from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} ({self.id})"
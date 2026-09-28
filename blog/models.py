from django.contrib import admin
from django.db import models
from blog.models import Person

# Create your models here.

@admin.register(Person)
class Person(models.Model):
    pass

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"

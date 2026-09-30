from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} ({self.id})"

class Post(models.Model):
    upload_now = models.BooleanField(default=False)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.author}, {self.title}"
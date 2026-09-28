from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"you have a message from {self.name}, {self.subject}"
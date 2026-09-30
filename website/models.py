from django.db import models
# Create your models here.

class Message(models.Model):
    status = models.BooleanField(default=False)
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"{self.name}, {self.subject}"
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

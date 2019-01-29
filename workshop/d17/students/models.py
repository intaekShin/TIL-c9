from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
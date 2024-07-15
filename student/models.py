from django.db import models
from django.db.models.manager import Manager

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField()
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    contact = models.CharField(max_length=20)
    bio = models.TextField()
    name = models.CharField(max_length=100, default='Default Name')
   

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    objects: Manager = models.Manager()




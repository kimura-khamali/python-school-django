from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length= 20)
    teacher_age = models.PositiveSmallIntegerField()
    teacher_id = models.PositiveSmallIntegerField()
    teacher_course = models.CharField(max_length=20)
    teacher_class = models.CharField(max_length=20)
    teacher_description = models.TextField()
    teacher_occupation = models.CharField(max_length=20)
    teacher_salary = models.PositiveSmallIntegerField()
    teacher_hobby = models.TextField()
    teacher_gender = models.CharField()

    
    
def __str__(self) -> str:
        return f"{self.teacher_name}"



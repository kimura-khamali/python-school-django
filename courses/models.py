from django.db import models

# Create your models here.


class Courses(models.Model):
    course_name= models.CharField(max_length=20)
    course_instructor = models.CharField(max_length=20)
    course_department = models.CharField(max_length=20)
    course_syllabus = models.CharField(max_length=20)
    course_code = models.PositiveSmallIntegerField()
    course_assigment = models.CharField(max_length=20)
    course_level = models.CharField(max_length=20)
    course_description = models.TextField()
    course_exams = models.CharField(max_length=20)
    course_duration = models.PositiveSmallIntegerField()



    def __str__(self) -> str:
        return f"{self.course_name}"
    






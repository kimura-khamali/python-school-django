from django.db import models

# Create your models here.


class Class_Period(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    name = models.CharField(max_length=100, default='Default Name')
    # class_id = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    class_period_classroom = models.CharField(max_length=20)
    class_period_course_taught = models.CharField(max_length=20)
    class_period_start_time = models.TimeField()
    class_period_end_time = models.TimeField()
    class_period_Day_of_the_week = models.CharField(max_length=20)

    objects = models.Manager()
   
    def __str__(self):
        return f"{self.class_period_course_taught} teaches {self.class_period_classroom}"


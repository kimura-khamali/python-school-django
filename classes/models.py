from django.db import models

class Classes(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    # class_name = models.CharField(max_length=20)
    name = models.CharField(max_length=100, default='Default Name')
    class_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=20)
    teacher_allocated = models.CharField(max_length=20)
    # course_taught = models.CharField(max_length=20)
    course_start_time = models.TimeField()
    course_end_time = models.TimeField()
    course_day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    seating_arrangement = models.JSONField(default=dict)
    equipment = models.JSONField(default=list)

    objects = models.Manager()
    def __str__(self):
        return f"{self.teacher_allocated} teaches {self.equipment}"
    


    
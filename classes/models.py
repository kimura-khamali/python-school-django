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
    


    # objects: Manager = models.Manager()




# from django.db import models

# class Classes(models.Model):
#     class_id = models.PositiveSmallIntegerField(primary_key=True)
#     room_number = models.CharField(max_length=20)
#     teacher_allocated = models.CharField(max_length=20)
#     course_tought = models.CharField(max_length=20)
#     course_start_time = models.TimeField()
#     course_end_time = models.TimeField()
#     course_day_of_week = models.CharField(max_length=20)
#     seating_arrangement = models.TextField()
#     equipment = models.TextField()


#     def __str__(self) -> str:
#         return f"{self.teacher_allocated} teaches {self.course_tought}"

    
# # String
# # Integer
# # String
# # String
# # Integer
# # String
# # String
# # String
# # Integer
# # String
# # String
# # Integer


    
    # class_rules = models.CharField(max_length=20)
    # class_capacity = models.PositiveSmallIntegerField()
    # class_perfomance = models.CharField(max_length=20)
    # class_lecturer = models.CharField(max_length=20)
    # class_id = models.PositiveSmallIntegerField()
    # class_name = models.CharField(max_length=20)
    # class_representative = models.CharField(max_length=20)
    # class_description = models.CharField()
    # class_table_number = models.PositiveSmallIntegerField()
    # class_bio = models.CharField(max_length=20)
    # class_rules = models.CharField(max_length=20)
    # student_id =models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')


# def __str__(self) -> str:
#       return f"{self.teacher_allocated} teaches {self.course_tought}"




from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20, null=True, blank=True)
    teacher_age = models.PositiveIntegerField()
    teacher_id = models.PositiveIntegerField()
    teacher_course = models.CharField(max_length=20)
    # teacher_class = models.CharField(max_length=20)
    teacher_description = models.TextField()
    teacher_occupation = models.CharField(max_length=20)
    teacher_salary = models.PositiveIntegerField()
    teacher_hobby = models.TextField()
    teacher_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # teacher_headshot = models.ImageField(upload_to='photo/')
    teacher_headshot = models.ImageField(default='default_teacher_headshot.jpg')
    
    objects = models.Manager()

    class Meta:
        ordering = ['teacher_name']

    def __str__(self):
        return f"{self.teacher_name}"
    
   
    

       
    





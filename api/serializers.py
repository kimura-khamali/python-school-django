from rest_framework import serializers
from student.models import Student
from classes.models import Classes
from courses.models import Courses
from teacher.models import Teacher
from class_period.models import Class_Period

class StudentSerializers(serializers.ModelSerializer):
      class Meta:
            model=Student
            fields='__all__'    


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields= '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'        



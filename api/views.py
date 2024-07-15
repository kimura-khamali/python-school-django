from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from class_period.models import Class_Period
from classes.models import Classes
from teacher.models import Teacher
from courses.models import Courses
from .serializers import StudentSerializers
from .serializers import TeacherSerializer
from .serializers import ClassesSerializer
from .serializers import Class_PeriodSerializer
from .serializers import CoursesSerializer
from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import serializers

class StudentListView(APIView):   
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)
    


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

     
class CoursesListView(APIView):
  def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)

class ClassesListView(APIView):
  def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)

class Classs_PeriodListView(APIView):
   def get(self, request):
        period = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(period, many=True)
        return Response(serializer.data)
   


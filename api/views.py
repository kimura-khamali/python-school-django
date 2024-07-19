from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from class_period.models import Class_Period
from classes.models import Classes
from teacher.models import Teacher
from courses.models import Courses
from rest_framework import status
from .serializers import StudentSerializers
from .serializers import TeacherSerializer
from .serializers import ClassesSerializer
from .serializers import Class_PeriodSerializer
from .serializers import CoursesSerializer
from rest_framework.response import Response



class StudentListView(APIView):   
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class StudentDetailView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer =StudentSerializers(student)
        return Response(serializer.data)   

    def put(self, request,id):
       student=Student.objects.get(id=id)
       serializer =StudentSerializers(student,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        student=Student.objects.get(id=id)
        serializer =StudentSerializers(student)
        student.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  


        

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        return Response(serializer.data)   

    def put(self, request,id):
       teacher=Teacher.objects.get(id=id)
       serializer =TeacherSerializer(teacher,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        teacher.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  


        


     
class CoursesListView(APIView):
  def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
  
  def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class CoursesDetailView(APIView):
    def get(self,request,id):
        courses=Student.objects.get(id=id)
        serializer =CoursesSerializer(courses)
        return Response(serializer.data)   

    def put(self, request,id):
       courses=Courses.objects.get(id=id)
       serializer =CoursesSerializer(courses,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        courses=Courses.objects.get(id=id)
        serializer =CoursesSerializer(courses)
        courses.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  


        

class ClassesListView(APIView):
  def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
  
  def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class ClassesDetailView(APIView):
    def get(self,request,id):
        classe=Classes.objects.get(id=id)
        serializer =ClassesSerializer(classe)
        return Response(serializer.data)   

    def put(self, request,id):
       classe=Classes.objects.get(class_id=id)
       serializer =ClassesSerializer(classe,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        classe=Classes.objects.get(id=id)
        serializer =ClassesSerializer(classe)
        classe.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  


        

class Classs_PeriodListView(APIView):
   def get(self, request):
        periods = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(periods, many=True)
        return Response(serializer.data)
   

   def post(self, request):
        serializer = Class_PeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class Class_PeriodDetailView(APIView):
    def get(self,request,id):
        period=Class_Period.objects.get(id=id)
        serializer =Class_PeriodSerializer(period)
        return Response(serializer.data)   

    def put(self, request,id):
       period=Class_Period.objects.get(class_id=id)
       serializer =Class_PeriodSerializer(period,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        period=Class_Period.objects.get(id=id)
        serializer =Class_PeriodSerializer(period)
        period.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  


        
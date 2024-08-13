# pylint: disable=invalid-name
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



# class StudentListView(APIView):   
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializers(students, many=True)
#         return Response(serializer.data)

# class StudentListView(APIView):   
#     def get(self, request):
#         students = Student.objects.all()
#         first_name = request.query_params.get("first_name")
#         if first_name:
#             students = students.filter(first_name = first_name)
#         serializer = StudentSerializers(students, many=True)
#         return Response(serializer.data)

class StudentListView(APIView):   
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")
        if first_name:
            students = students.filter(first_name = first_name)
        if country:
            students = students.filter(country = country)
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

    def enroll_student(self,student,course_id):
        course = Courses.objects.get(id=course_id)
        student.courses.add(course)

    def unenroll_student(self,student,course_id):
        course = Courses.objects.get(id=course_id)
        student.courses.remove(course)    

    
    def add_to_class(self, student, class_id):
        class_obj = Classes.objects.get(id=class_id)
        student.classes.add(class_obj)    

    def post(self,request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action") 

        if action == "enroll":
           course_id = request.data.get("course")
           self.enroll_student(student,course_id)
           return Response(status.HTTP_202_ACCEPTED)
        
        if action == "unenroll":
           course_id = request.data.get("course")
           self.unenroll_student(student,course_id)
           return Response(status.HTTP_202_ACCEPTED)
        
        elif action == "add_to_class":
            class_id = request.data.get("classes")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_202_ACCEPTED)


    # def post(self, request, id):
    #     student = Student.objects.get(id=id)
    #     action = request.data.get("action")

        # if action == "enroll":
        #     course_id = request.data.get("course")
        #     self.enroll_student(student, course_id)
        #     return Response(status=status.HTTP_202_ACCEPTED)
        
        # elif action == "unenroll":
        #     course_id = request.data.get("course")
        #     self.unenroll_student(student, course_id)
        #     return Response(status=status.HTTP_202_ACCEPTED)
        
        # elif action == "add_to_class":
        #     class_id = request.data.get("classes")
        #     self.add_to_class(student, class_id)
        #     return Response(status=status.HTTP_202_ACCEPTED)

        # return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
    # def get_class(self,student,classes_id):
    #     classess = Classes.objects.get(id-classes_id)  
    #     student.classes.add(classess)

        

        # if assigned == "Add in class":  
        #    classes_id = req 

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = TeacherSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def assign_course(self, teacher, course_id):
        course = Courses.objects.get(id=course_id)
        teacher.courses.add(course)

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")

        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response({"message": "Teacher assigned to course successfully"}, status=status.HTTP_202_ACCEPTED)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
        

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


        
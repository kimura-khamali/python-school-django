# from django.urls import path
# # from .views import StudentRegistrationForm
# from . import views


# # urlpatterns = [
# #     path('register/',views.register_Student,name='register_Student'),

# # ]

# urlpatterns = [
# #     path('register/', views.register_Student, name='register_Student'),
#       path('api/students/register/', views.student_register_view, name='student_register_view'),

#  ]


from django.urls import path
from .views import student_register_view

urlpatterns = [
    path('register/', student_register_view, name='student_register_view'),
]



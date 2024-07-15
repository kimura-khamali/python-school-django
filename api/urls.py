# from django.urls import path
# from .views import StudentListView
# from .views import TeacherListView
# from .views import CoursesListView
# from .views import ClassesListView
# from .views import Classs_PeriodListView


# urlpatterns = [
#     path("students/", StudentListView.as_view(), name='student_List_Views'),
#     path("teachers/", TeacherListView.as_view(), name='teacher_List_Views'),
#     path("Classes/", ClassesListView.as_view())
   
# ]



from django.urls import path
from .views import StudentListView, TeacherListView, CoursesListView, ClassesListView, Classs_PeriodListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('teachers/', TeacherListView.as_view, name='teacher_list_view'),
    path('classes/', ClassesListView.as_view(), name='classes_list_view'),
    path('courses/', CoursesListView.as_view(), name='courses_list_view'),
    path('class-periods/', Classs_PeriodListView.as_view(), name='class_period_list_view')
]



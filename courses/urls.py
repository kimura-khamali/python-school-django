from django.urls import path
from .views import courses_register_view

urlpatterns = [
    path('register/', courses_register_view, name='courses_register_view'),
]


from django.urls import path

from .views import teacher_register_view


urlpatterns = [
    path('register/', teacher_register_view, name='teacher_register_view'),
]


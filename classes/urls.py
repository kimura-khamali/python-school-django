from django.urls import path
from .views import classes_register_view

urlpatterns = [
    path('register/', classes_register_view, name='classes_register_view'),
]

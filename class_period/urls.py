from django.urls import path
from .views import class_period_register_view

urlpatterns = [
    path('register/', class_period_register_view, name='class_period_register_view'),
]

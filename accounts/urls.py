from django.urls import path
from .views import user_login, user_logout
from accounts import views

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', views.home_view, name='home'),
    # path('', views.home_view, name='home'),
]
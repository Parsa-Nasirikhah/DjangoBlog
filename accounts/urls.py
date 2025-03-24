from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin', views.auth_login, name='login'),
    path('logout', views.auth_logout, name='logout')
]
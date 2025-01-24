from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('update_age/<int:student_id>/', views.update_age, name='update_age'),
]
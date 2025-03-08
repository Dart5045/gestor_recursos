from django.urls import path
from . import views

app_name = 'classrooms'

urlpatterns = [
    path('', views.list_classrooms, name='list'),
    path('create/', views.create_classroom, name='create'),
    path('edit/<int:id>/', views.edit_classroom, name='edit'),
    path('delete/<int:id>/', views.delete_classroom, name='delete'),
]
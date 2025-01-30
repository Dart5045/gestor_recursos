from django.urls import path
from . import views

app_name = 'classrooms'

urlpatterns = [
    path('', views.list_classrooms, name='list_classrooms'),
    path('create/', views.create_classroom, name='create_classroom'),
    path('edit/<int:id>/', views.edit_classroom, name='edit_classroom'),
    path('delete/<int:id>/', views.delete_classroom, name='delete_classroom'),
]
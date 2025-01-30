from django.urls import path
from . import views

urlpatterns = [
    path('', views.resources_list, name='resources_list'),
]

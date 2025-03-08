from django.urls import path
from . import views


urlpatterns = [
    path('', views.vulnerable_login, name='login'),  # Login
    path('login_form/', views.login_form, name='login_form'),  # Formulario de inicio de sesión
    path('login/', views.custom_login, name='login'),  # Manejo del inicio de sesión
    path('logout/', views.custom_logout, name='logout'),  # Cierre de sesión
]
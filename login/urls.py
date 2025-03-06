from django.urls import path
from .views import vulnerable_login


urlpatterns = [
    path('', vulnerable_login, name='login'),  # Login
]
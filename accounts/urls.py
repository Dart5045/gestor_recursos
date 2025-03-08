from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
]
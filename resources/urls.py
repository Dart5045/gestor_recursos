from django.urls import path
from .views import ResourceListView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView
app_name = 'resources' 
urlpatterns = [
    #path('', views.resources_list, name='resources_list'),
    path('', ResourceListView.as_view(), name='list'),
    path('create/', ResourceCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ResourceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ResourceDeleteView.as_view(), name='delete'),
]

from django.shortcuts import render
from .models import Resource
# Create your views here.

def resources_list(request):
    resources = Resource.objects.raw("SELECT * FROM resources_resource WHERE name = '%s'" % request.GET['name'])
    return render(request, 'resources/list.html', {'resources': resources})
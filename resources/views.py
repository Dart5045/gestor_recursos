from django.shortcuts import render
from .models import Resource
# Create your views here.


# Vista sin control de acceso
def view_resource(request, resource_id):
    resource = Recurso.objects.get(id=resource_id)
    return render(request, 'resources/view_resource.html', {'recurso': resource})

def resources_list(request):
    resources = Resource.objects.raw("SELECT * FROM resources_resource WHERE name = '%s'" % request.GET['name'])
    return render(request, 'resources/list.html', {'resources': resources})
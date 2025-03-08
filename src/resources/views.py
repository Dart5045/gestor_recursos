from django.shortcuts import render
from .models import Resource
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ResourceForm


# Vista sin control de acceso
def view_resource(request, resource_id):
    resource = Recurso.objects.get(id=resource_id)
    return render(request, 'resources/view_resource.html', {'recurso': resource})

def resources_list(request):
    resources = Resource.objects.raw("SELECT * FROM resources_resource WHERE name = '%s'" % request.GET['name'])
    return render(request, 'resources/list.html', {'resources': resources})

# Vista para listar recursos
class ResourceListView(ListView):
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'

# Vista para crear un nuevo recurso
class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resources/resource_form.html'
    success_url = reverse_lazy('resources:list')

# Vista para editar un recurso existente
class ResourceUpdateView(UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resources/resource_form.html'
    success_url = reverse_lazy('resources:list')

# Vista para eliminar un recurso
class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = 'resources/resource_confirm_delete.html'
    success_url = reverse_lazy('resources:list')
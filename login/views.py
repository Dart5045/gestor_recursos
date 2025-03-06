# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django_elasticsearch_dsl.registries import registry
from .documents import UserDocument
from django.utils.timezone import now

def vulnerable_login(request):
    ip_address = request.META.get('REMOTE_ADDR')  # Obtiene la dirección IP del usuario
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        # Registrar evento de login (exitoso o fallido)
        if user is not None:
            login(request, user)
            success = True
        else:
            success = False

        # Aquí se pueden realizar otras acciones, como registrar eventos en un log
        # Actualizamos o indexamos el evento en Elasticsearch
        user_document = UserDocument.search().filter('term', username=username).first()
        if user_document:
            # Puedes agregar la lógica para indexar más detalles, por ejemplo, el timestamp del evento
            user_document.update({'last_login_attempt': now(), 'success': success})
        
        # Guardamos el evento en Elasticsearch para monitorearlo
        if success:
            # Indexar el evento de login exitoso en Elasticsearch
            UserDocument().update(user)
            return redirect('/dashboard/')
        else:
            # Indexar el evento de login fallido en Elasticsearch
            UserDocument().update(user)
            return HttpResponse('Credenciales inválidas')
    
    return render(request, 'login/vulnerable_login.html')
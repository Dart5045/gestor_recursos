from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django_elasticsearch_dsl.registries import registry
from django.utils.timezone import now
from .documents import UserDocument

def vulnerable_login(request):
    ip_address = request.META.get('REMOTE_ADDR')  # Obtiene la dirección IP del usuario

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        success = user is not None  # True si el login es exitoso, False si falla

        if success:
            login(request, user)

        # Buscar si el usuario ya está indexado en Elasticsearch
        try:
            user_document = UserDocument.get(id=user.id) if success else None
        except UserDocument.DoesNotExist:
            user_document = None

        # Si el documento existe, actualizarlo; si no, crearlo
        if user_document:
            user_document.last_login_attempt = now()
            user_document.login_success = success
            user_document.ip_address = ip_address
        else:
            user_document = UserDocument(
                meta={'id': user.id if success else f"failed-{username}-{now().timestamp()}"},
                username=username,
                first_name=user.first_name if success else '',
                last_name=user.last_name if success else '',
                email=user.email if success else '',
                last_login_attempt=now(),
                login_success=success,
                ip_address=ip_address,
            )

        # Guardar en Elasticsearch
        user_document.save()

        if success:
            return redirect('/dashboard/')
        else:
            return HttpResponse('Credenciales inválidas')

    return render(request, 'login/vulnerable_login.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django_elasticsearch_dsl.registries import registry
from django.utils.timezone import now
from .documents import UserDocument

def vulnerable_login(request):
    ip_address = request.META.get('REMOTE_ADDR')  

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        success = user is not None  

        if success:
            login(request, user)

            # Registrar solo logins exitosos para no exponer intentos fallidos
            user_document, created = UserDocument.get_or_create(id=user.id, defaults={
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            })

            # Actualizar último login exitoso
            user_document.last_login_attempt = now()
            user_document.save()

            return redirect('/dashboard/')
        else:
            # No almacenamos intentos fallidos con detalles de usuario por privacidad
            return HttpResponse('Credenciales inválidas')

    return render(request, 'login/vulnerable_login.html')

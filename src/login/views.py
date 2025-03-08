from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now
from .documents import UserDocument

def log_login_attempt(username, success, ip_address):
    """ Registra intentos de login (exitosos o fallidos) en Elasticsearch """
    user_log = UserDocument(
        username=username,
        last_login_attempt=now(),
        login_success=success,
        ip_address=ip_address
    )
    user_log.save()

def login_form(request):
    return render(request, 'login/vulnerable_login.html')

def vulnerable_login(request):
    ip_address = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        success = user is not None  # True si la autenticación fue correcta

        # Registrar intento de login en Elasticsearch
        log_login_attempt(username, success, ip_address)

        if success:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Credenciales inválidas')

    return render(request, 'login/vulnerable_login.html')

def custom_logout(request):
    logout(request)
    return render(request, 'login/logout.html')

def custom_login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.get(username=username)
        # No se recomienda guardar contraseñas en texto plano
        if user.password == password:
            login(request, user)  # Llama al método login correctamente
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('dashboard') 
    except User.DoesNotExist:
        # Error de autenticación
        messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'dashboard/login_form.html')
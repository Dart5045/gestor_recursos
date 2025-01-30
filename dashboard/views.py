from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
 
def index(request):
    return render(request, 'dashboard/index.html')

def custom_logout(request):
    logout(request)
    return render(request, 'dashboard/logout.html')

def login_form(request):
    return render(request, 'dashboard/login_form.html')

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
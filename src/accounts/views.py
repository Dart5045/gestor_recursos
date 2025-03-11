from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django import forms

# Formulario inseguro
class InsecureUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# Vista de registro insegura
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)  # No se encripta la contraseña
        return redirect('/')
    return render(request, 'accounts/register.html')

# Listar usuarios
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

# Eliminar usuario
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('accounts:user_list')

# Editar usuario sin seguridad
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.password = request.POST['password']  # No usa set_password()
        user.save()
        return redirect('accounts:user_list')
    return render(request, 'accounts/user_edit.html', {'user': user})
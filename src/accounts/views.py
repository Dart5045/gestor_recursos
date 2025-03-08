from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'accounts/register.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

def user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user_list')

def user_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.set_password(request.POST['password'])
        user.save()
        return redirect('user_list')
    return render(request, 'accounts/user_edit.html', {'user': user})
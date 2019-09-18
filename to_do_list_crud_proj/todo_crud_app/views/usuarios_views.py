from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastrar_usuarios(request):
    if request.method == "POST":
        form_usuarios = UserCreationForm(request.POST)
        if form_usuarios.is_valid():
            form_usuarios.save()
        return redirect('listar_tarefas')
    else:
        form_usuarios = UserCreationForm()
    return render(request, 'usuarios/form_usuarios.html', {"form_usuarios":form_usuarios})

def login_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        usuario = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_tarefas')
        else:
            messages.error(request, 'Login Incorreto. Verificar e Tentar Novamente!')
            return redirect('login_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect(login_usuario)
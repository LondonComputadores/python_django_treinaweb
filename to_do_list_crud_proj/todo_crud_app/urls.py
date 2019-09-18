from django.contrib import admin
from django.urls import path
from .views.tarefa_views import *
from .views.usuarios_views import *

urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefas/', cadastrar_tarefas, name='cadastrar_tarefas'),
    path('editar_tarefa/<int:id>', editar_tarefa, name='editar_tarefa'),
    path('remover_tarefa/<int:id>', remover_tarefa, name='remover_tarefa'),
    path('cadastrar_usuarios/', cadastrar_usuarios, name='cadastrar_usuarios'),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
]
from django.shortcuts import render
from .forms import TarefaForm

# Create your views here.

def listar_tarefas(request):
    nome_tarefa = "Assistir a Semana Python e Django da Treinaweb"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})

def cadastrar_tarefas(request):
    form_tarefas = TarefaForm()
    return render(request, 'tarefas/form_tarefas.html', {"form_tarefas": form_tarefas})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import TarefaForm
from ..entidades.tarefa import Tarefa
from ..services import tarefas_services

# Create your views here.

@login_required()
def listar_tarefas(request):
    tarefas = tarefas_services.listar_tarefas()
    # nome_tarefa = "Assistir a Semana Python e Django da Treinaweb"
    # return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})

    return render(request, 'tarefas/listar_tarefas.html', {"tarefas": tarefas})

@login_required()
def cadastrar_tarefas(request):
    if request.method == "POST":
        form_tarefas = TarefaForm(request.POST)
        if form_tarefas.is_valid():
            titulo = form_tarefas.cleaned_data["titulo"]
            descricao = form_tarefas.cleaned_data["descricao"]
            data_expiracao = form_tarefas.cleaned_data["data_expiracao"]
            prioridade = form_tarefas.cleaned_data["prioridade"]
            tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, 
                                  prioridade=prioridade, usuario=request.user)
            tarefas_services.cadastrar_tarefas(tarefa_nova)
            return redirect('listar_tarefas')
    else:
        form_tarefas = TarefaForm()
    return render(request, 'tarefas/form_tarefas.html', {"form_tarefas": form_tarefas})

@login_required()
def editar_tarefa(request, id):
    tarefa_bd = tarefas_services.listar_tarefas_id(id)
    if tarefa_bd.usuario != request.user:
        return HttpResponse("Não Permitido!")
    form_tarefas = TarefaForm(request.POST or None, instance=tarefa_bd)
    if form_tarefas.is_valid():
        titulo = form_tarefas.cleaned_data["titulo"]
        descricao = form_tarefas.cleaned_data["descricao"]
        data_expiracao = form_tarefas.cleaned_data["data_expiracao"]
        prioridade = form_tarefas.cleaned_data["prioridade"]
        tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, 
                                  prioridade=prioridade, usuario=request.user)
        tarefas_services.editar_tarefa(tarefa_bd, tarefa_nova)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/form_tarefas.html', {"form_tarefas": form_tarefas})

@login_required()
def remover_tarefa(request, id):
    tarefa_bd = tarefas_services.listar_tarefas_id(id)
    if request.method == "POST":
        tarefas_services.remover_tarefas_id(id)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/confirma_exclusao.html', {"tarefas": tarefa_bd})






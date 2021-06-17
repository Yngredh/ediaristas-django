from django.shortcuts import render, redirect
from .forms import diarista_form
from .models import Diarista

# Create your views here.

def cadastrar_diarista(request):
    if request.method == "POST":
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm()
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})

def listar_diaristas(request):
    diaristas = Diarista.objects.all()
    return render(request, 'lista_diaristas.html', {'diaristas': diaristas})

def editar_diarista(request, diarista_id):
    diarista = Diarista.objects.get(id=diarista_id)
    if request.methos == "POST":
        # Uma vez que a diarista já está cadastrada, o metodo da requisição será 'post' e não 'get'
        form_diarista = diarista_form.DiaristaForm(request.POST or None, request.FILED, instance=diarista)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        # Cria um formulário com os dados preenchidos(db) da diarista
        form_diarista = diarista_form.DiaristaForm(instance=diarista)
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})

def remover_diarista (request, diarista_id):
    diarista = Diarista.objects.get(id=diarista_id)
    diarista.delete()
    return redirect('listar_diaristas')
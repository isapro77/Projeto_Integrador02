from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def agendamento(request):
    return render(request, 'agendamento.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def consulta(request):
    return render(request, 'consulta.html')

def galeria(request):
    return render(request, 'galeria.html')



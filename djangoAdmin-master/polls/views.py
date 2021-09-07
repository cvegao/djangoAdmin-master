from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'polls/home.html')


def clientes(request):
    clientes = Client.objects.all()
    data = {
        'clientes': clientes,

    }
    return render(request, 'polls/cliente.html', data)


def sitios(request):
    sitios = Site.objects.all()
    data = {
        'sitios': sitios,
    }
    return render(request, 'polls/sitios.html', data)


def leads(request):
    leads = Lead.objects.all()
    data = {
        'leads': leads,
    }
    return render(request, 'polls/lead.html', data)


def documentos(request):
    doctos = Documento.objects.all()
    data = {
        'doctos': doctos,
    }
    return render(request, 'polls/documento.html', data)


def libros_publicadores(request):
    libros = Libro.objects.all()
    publicadores = Publicador.objects.all()
    data = {
        'libros': libros,
        'publicadores': publicadores,
    }
    return render(request, 'polls/libros_publicadores.html', data)


def edit_libros_publicadores_form(request):
    id = request.POST['id']
    print(id)


def delete_libros_publicadores_form(request):
    pass

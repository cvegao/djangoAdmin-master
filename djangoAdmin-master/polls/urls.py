from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('sitios/', views.sitios, name='sitios'),
    path('lead/', views.leads, name='lead'),
    path('doctos/', views.documentos, name='doctos'),
    path('libros_publicadores/', views.libros_publicadores, name='libros_publicadores'),
    path('libros_publicadores/edit_publicador', views.edit_libros_publicadores_form, name='edit_publicador'),
    path('libros_publicadores/delete_publicador', views.delete_libros_publicadores_form, name='delete_publicador'),
]

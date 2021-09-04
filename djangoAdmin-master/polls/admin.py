from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(Site)
admin.site.register(Lead)
admin.site.register(Documento)

class Meta:
    title = 'Administrador de Clientes'
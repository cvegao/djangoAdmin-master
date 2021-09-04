from django.contrib import admin
from .models import *
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email')
    list_filter =('joined_datetime',)
    search_fields =('email',)

admin.site.register(Client,ClientAdmin)
admin.site.register(Site)
admin.site.register(Lead)
admin.site.register(Documento)


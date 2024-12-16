from django.contrib import admin
from .models import Documento, Tipo_doc
# Register your models here.

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('name_doc', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('name_doc', "tipo__name")

# Register your models here.
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Tipo_doc)
from django.contrib import admin
from .models import Maquinaria, Mantencion, Repuesto

admin.site.register(Maquinaria)
admin.site.register(Mantencion)
admin.site.register(Repuesto)

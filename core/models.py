from django.db import models
from django.contrib.auth.models import User

class Maquinaria(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    estado = models.CharField(max_length=50, choices=[
        ("operativa", "Operativa"),
        ("en_reparacion", "En reparación"),
        ("fuera_servicio", "Fuera de servicio"),
    ])

    def __str__(self):
        return self.nombre


class Repuesto(models.Model):
    nombre = models.CharField(max_length=120)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock})"


class Mantencion(models.Model):
    maquinaria = models.ForeignKey(Maquinaria, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=[
        ("preventiva", "Preventiva"),
        ("correctiva", "Correctiva"),
        ("predictiva", "Predictiva")
    ])
    fecha_programada = models.DateField()
    fecha_realizada = models.DateField(null=True, blank=True)
    descripcion = models.TextField()
    tecnico_responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    repuestos = models.ManyToManyField(Repuesto, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.maquinaria.nombre}"

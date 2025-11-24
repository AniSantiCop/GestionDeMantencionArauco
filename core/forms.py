from django import forms
from .models import Maquinaria, Mantencion, Repuesto

class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = "__all__"
        widgets = {
            "fecha_adquisicion": forms.DateInput(attrs={"type": "date"})
        }

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantencion
        fields = "__all__"
        widgets = {
            "fecha_programada": forms.DateInput(attrs={"type": "date"}),
            "fecha_realizada": forms.DateInput(attrs={"type": "date"}),
        }

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = "__all__"
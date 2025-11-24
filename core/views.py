from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Maquinaria, Mantencion, Repuesto
from .forms import MaquinariaForm, MantencionForm, RepuestoForm

# --- Dashboard ---
@login_required
def dashboard(request):
    maquinas = Maquinaria.objects.count()
    mant_pendientes = Mantencion.objects.filter(fecha_realizada__isnull=True).count()
    return render(request, "dashboard.html", {
        "maquinas": maquinas,
        "mant_pendientes": mant_pendientes
    })

# --- MAQUINARIA CRUD ---
@login_required
def maquinaria_list(request):
    maquinas = Maquinaria.objects.all()
    return render(request, "maquinaria_list.html", {"maquinas": maquinas})

@login_required
def maquinaria_create(request):
    form = MaquinariaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Maquinaria creada correctamente")
        return redirect("maquinaria_list")
    return render(request, "maquinaria_form.html", {"form": form})

@login_required
def maquinaria_update(request, pk):
    maquina = get_object_or_404(Maquinaria, pk=pk)
    form = MaquinariaForm(request.POST or None, instance=maquina)
    if form.is_valid():
        form.save()
        messages.success(request, "Maquinaria actualizada")
        return redirect("maquinaria_list")
    return render(request, "maquinaria_form.html", {"form": form})

@login_required
def maquinaria_delete(request, pk):
    maquina = get_object_or_404(Maquinaria, pk=pk)
    maquina.delete()
    messages.success(request, "Maquinaria eliminada")
    return redirect("maquinaria_list")

# --- MANTENCIONES CRUD ---
@login_required
def mantencion_list(request):
    mantenciones = Mantencion.objects.all()
    return render(request, "mantencion_list.html", {"mantenciones": mantenciones})

@login_required
def mantencion_create(request):
    form = MantencionForm(request.POST or None)
    if form.is_valid():
        mantencion = form.save(commit=False)
        mantencion.tecnico_responsable = request.user
        mantencion.save()
        form.save_m2m()  # Para guardar los repuestos ManyToMany
        messages.success(request, "Mantención registrada")
        return redirect("mantencion_list")
    return render(request, "mantencion_form.html", {"form": form})

@login_required
def mantencion_update(request, pk):
    mant = get_object_or_404(Mantencion, pk=pk)
    form = MantencionForm(request.POST or None, instance=mant)
    if form.is_valid():
        form.save()
        messages.success(request, "Mantención actualizada")
        return redirect("mantencion_list")
    return render(request, "mantencion_form.html", {"form": form})

@login_required
def mantencion_delete(request, pk):
    mant = get_object_or_404(Mantencion, pk=pk)
    mant.delete()
    messages.success(request, "Mantención eliminada")
    return redirect("mantencion_list")

# --- REPUESTOS CRUD ---
@login_required
def repuesto_list(request):
    repuestos = Repuesto.objects.all()
    return render(request, "repuesto_list.html", {"repuestos": repuestos})

@login_required
def repuesto_create(request):
    form = RepuestoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Repuesto creado correctamente")
        return redirect("repuesto_list")
    return render(request, "repuesto_form.html", {"form": form})

@login_required
def repuesto_update(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    form = RepuestoForm(request.POST or None, instance=repuesto)
    if form.is_valid():
        form.save()
        messages.success(request, "Repuesto actualizado")
        return redirect("repuesto_list")
    return render(request, "repuesto_form.html", {"form": form})

@login_required
def repuesto_delete(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    repuesto.delete()
    messages.success(request, "Repuesto eliminado")
    return redirect("repuesto_list")

# --- PROFILE ---
@login_required
def profile(request):
    return render(request, 'profile.html')
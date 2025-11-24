from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # MAQUINARIA CRUD
    path("maquinaria/", views.maquinaria_list, name="maquinaria_list"),
    path("maquinaria/nueva/", views.maquinaria_create, name="maquinaria_create"),
    path("maquinaria/editar/<int:pk>/", views.maquinaria_update, name="maquinaria_update"),
    path("maquinaria/eliminar/<int:pk>/", views.maquinaria_delete, name="maquinaria_delete"),

    # MANTENCIONES CRUD
    path("mantenciones/", views.mantencion_list, name="mantencion_list"),
    path("mantenciones/nueva/", views.mantencion_create, name="mantencion_create"),
    path("mantenciones/editar/<int:pk>/", views.mantencion_update, name="mantencion_update"),
    path("mantenciones/eliminar/<int:pk>/", views.mantencion_delete, name="mantencion_delete"),

    # REPUESTOS CRUD
    path("repuestos/", views.repuesto_list, name="repuesto_list"),
    path("repuestos/nuevo/", views.repuesto_create, name="repuesto_create"),
    path("repuestos/<int:pk>/editar/", views.repuesto_update, name="repuesto_update"),
    path("repuestos/<int:pk>/eliminar/", views.repuesto_delete, name="repuesto_delete"),

    # PROFILE
    path('profile/', views.profile, name='profile'),
]
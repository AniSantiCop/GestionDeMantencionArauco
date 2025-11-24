Sistema de Gestión Forestal - INACAP
Evaluación N°3: Programación Backend - T13041

## Descripción del Proyecto
Sistema web desarrollado en Django para la gestión integral de maquinaria, mantenimientos y repuestos en el sector forestal. Esta aplicación responde a los requerimientos de la Evaluación N°3 de Programación Backend, simulando un encargo real de una empresa del rubro forestal/logístico del Biobío.

## Arquitectura del Sistema
text
mantenciones/
├── core/                          # Aplicación principal
│   ├── models.py                  # Modelos: Maquinaria, Mantencion, Repuesto
│   ├── views.py                   # Vistas CRUD + Dashboard
│   ├── forms.py                   # Formularios Django
│   ├── urls.py                    # Routing de la aplicación
│   └── templates/                 # Templates HTML
├── mantenciones/                  # Configuración del proyecto
│   ├── settings.py               # Configuración Django + BD
│   └── urls.py                   # URLs globales
├── requirements.txt              # Dependencias del proyecto
└── .env                         # Variables de entorno (no versionado)

## Modelo de Datos
python
# 3 Entidades principales con relaciones
Maquinaria (1) ──────── (N) Mantencion (N) ──────── (N) Repuesto
    │                           │
    └─ nombre, tipo, estado     └─ tipo, fechas, técnico

## Instalación y Configuración
1. Crear y Activar Entorno Virtual
bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (Linux/Mac)
source venv/bin/activate
2. Instalar Dependencias
bash
pip install -r requirements.txt
3. Configurar Variables de Entorno
Crear archivo .env en la raíz del proyecto:

ini
# Database Configuration
DB_NAME=mantenciones_db
DB_USER=root
DB_PASSWORD=tu_password_mysql
DB_HOST=localhost
DB_PORT=3306

# Django Configuration
SECRET_KEY=tu_clave_secreta_django_muy_segura
DEBUG=True
4. Configurar Base de Datos MariaDB/MySQL
sql
-- Conectar a MySQL/MariaDB
mysql -u root -p

-- Crear base de datos
CREATE DATABASE mantenciones_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Verificar creación
SHOW DATABASES;
5. Migraciones de Base de Datos
bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
6. Crear Superusuario
bash
python manage.py createsuperuser

# Seguir las instrucciones:
# Username: admin
# Email: admin@inacap.cl
# Password: ********
7. Ejecutar Servidor de Desarrollo
bash
python manage.py runserver
El sistema estará disponible en: http://127.0.0.1:8000

## Uso del Sistema
Funcionalidades Principales:
Dashboard: Vista general con estadísticas del sistema

Gestión de Maquinaria: CRUD completo de equipos forestales

Control de Mantenciones: Programación y registro de mantenimientos

Inventario de Repuestos: Administración de stock y precios

Sistema de Autenticación: Login seguro con sesiones

Flujo de Trabajo:
Iniciar sesión con credenciales de administrador

Registrar maquinaria en el sistema

Programar mantenimientos preventivos/correctivos

Gestionar repuestos utilizados en mantenimientos

Seguimiento de mantenimientos pendientes/completados

## Cumplimiento de Rúbrica de Evaluación
2.1.1 Configura conexión a BD
Conexión MySQL configurada con variables de entorno

Configuración segura en settings.py

Migraciones aplicadas correctamente

2.1.3 Codifica funciones CRUD
3 entidades operacionales (sobrecumplido)

Validaciones de datos en formularios

Manejo de errores y mensajes de usuario

2.1.4 Aplicación backend segura
Sistema de autenticación Django

Protección de rutas con @login_required

Hash seguro de contraseñas

Arquitectura MVC organizada

## Documentación del proyecto
README.md con instrucciones de instalación

Código comentado y estructurado

Modelo de datos documentado

## Calidad del código
Código modular y reutilizable

Buenas prácticas de desarrollo

Proyecto ejecutable sin modificaciones

Estructura Django estándar

## Tecnologías Implementadas
Backend: Django 5.2.8 + Python

Base de Datos: MariaDB/MySQL

Frontend: HTML5 + Bootstrap 5 + CSS3

Seguridad: Sistema de autenticación Django

Iconos: Bootstrap Icons

Variables de Entorno: python-dotenv

## Características Técnicas Destacadas
Diseño Responsive: Interfaz adaptable a dispositivos móviles

Validaciones: Formularios con validación tanto frontend como backend

Relaciones Complejas: Modelos con ForeignKey y ManyToMany

Sistema de Mensajes: Feedback al usuario mediante Django messages

Seguridad: Protección CSRF, hash de contraseñas, sanitización de datos

## Contexto Académico
Este proyecto fue desarrollado para la Evaluación N°3 de la asignatura Programación Backend - T13041 en INACAP, demostrando competencias en:

Desarrollo de aplicaciones web con Django

Gestión de bases de datos relacionales

Implementación de sistemas de autenticación

Aplicación de principios de seguridad web

Documentación de proyectos de software

## Información del Estudiante
Carrera: Analista Programador

Nombre del/la desarrollador: Ana Santibáñez

Asignatura: Programación Backend - T13041

Sede: INACAP San Pedro de la Paz

Año: 2025
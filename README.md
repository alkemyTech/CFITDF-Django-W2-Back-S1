# CFITDF-Django-W2-Back-S1
Repositorio Back Squad 1 | Django | CFI TDF 25

# App de Reservas
Aplicación web desarrollada en Django para gestionar la reserva de servicios ofrecidos por una empresa de eventos. El sistema permite registrar servicios, empleados, coordinadores, clientes, y realizar reservas, con funcionalidades de consulta tanto desde la interfaz web como desde una API REST.

## Objetivo General
El sistema busca resolver las siguientes necesidades:

- Registrar servicios ofrecidos por la empresa.
- Registrar empleados y clientes.
- Permitir a los empleados registrar reservas.
- Visualizar distintos listados de información.
- Exponer un endpoint para consultar los servicios disponibles y acceder a su detalle.
## Requisitos
- **Python 3.10 o superior**
- **Git**
## Instalación

### 1. Clonar el repositorio
```bash
# Clonar el repositorio
git clone "https://github.com/alkemyTech/CFITDF-Django-W2-Back-S1" 
# Ingresar a la carpeta del proyecto
cd CFITDF-Django-W2-Back-S1
```

### 2. Crear y Activar el entorno virtual
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Crear superusuario
Para acceder a la interfaz de administración de Django, creá un superusuario: 
```bash
python manage.py createsuperuser
```

### 5. Iniciar el servidor
```bash
python manage.py runserver
```
## Acceso a la App
Una vez el servidor esté en ejecución, podes acceder a la aplicación desde:
- Aplicación: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
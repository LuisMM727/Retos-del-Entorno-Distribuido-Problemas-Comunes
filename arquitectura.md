# Documentación de Arquitectura de Software

## Patrón de Diseño
El módulo utiliza la arquitectura Modelo-Vista-Template (MVT) nativa de Django

gestion_gastos/
│
├── gestion_gastos/          # Configuración global del proyecto
│   ├── __init__.py
│   ├── settings.py          # Configuración de BD y Apps
│   ├── urls.py              # Rutas globales
│   └── wsgi.py
│
├── gastos/                  # Aplicación principal del módulo
│   ├── migrations/          # Historial de migraciones de la BD
│   ├── models.py            # Definición de entidades 
│   ├── views.py             # Lógica del modulo
│   ├── urls.py              # Enrutamiento local
│   └── templates/           # Vistas e interfaz HTML
│
├── manage.py                # Script ejecutable de Django
├── README.md                # Documentación de instalacion y entorno
└── arquitectura.md          # Este documento de arquitectura

  
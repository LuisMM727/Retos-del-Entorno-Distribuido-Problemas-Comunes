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
├── gastos/                  # Aplicación del módulo
│   ├── migrations/          # Historial de migraciones SQL
│   ├── models.py            # Mapeo ORM y definición de entidades
│   ├── views.py             # Lógica de procesamiento y respuesta
│   ├── urls.py              # Enrutamiento local del módulo
│   └── templates/           # Vistas HTML / Interfaz gráfica
│
├── manage.py                # Script de gestión del proyecto
├── README.md
└── arquitectura.md
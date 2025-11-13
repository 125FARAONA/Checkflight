Descripción del Proyecto

CheckFlight es un simulador de app web de gestión de vuelos orientado a pasajeros y tripulación, con un enfoque principal en un checklist interactivo de tareas pre-vuelo y post-vuelo.

La app permite a los usuarios:

Iniciar sesión con credenciales simuladas.

Seleccionar un vuelo de manera interactiva.

Visualizar un dashboard de vuelo con los datos del viaje.

Completar un checklist de preparación de vuelo, incluyendo tareas como Check-in online, documentos listos, maleta preparada y abordaje completado.

Finalizar el vuelo con una animación y mensaje de éxito: "¡Feliz vuelo! Vamo arriba 🚀".

El checklist de tareas es el núcleo de la aplicación, demostrando cómo la lógica y la gestión de estados pueden integrarse en aplicaciones prácticas para aerolíneas.

Estructura del Proyecto
checklist_vuelo/
│
├── app.py                     # Archivo principal del servidor Flask
├── requirements.txt           # Lista de dependencias
│
├── static/                    # Archivos estáticos (CSS, imágenes, JS)
│   ├── style.css
│   └── logo_arajet.png
│
└── templates/                 # Vistas HTML
    ├── login.html
    ├── dashboard.html
    ├── checklist.html
    └── completed.html

Tecnologías y Herramientas

Python 3.13 - Lógica y backend con Flask.

Flask - Framework ligero para aplicaciones web.

HTML/CSS - Interfaces interactivas y diseño responsivo.

JavaScript (opcional) - Animaciones y mejoras de UX.

Logo y colores de Arajet - Para identidad visual y realismo.

Características Principales

Login seguro

Validación de usuario y contraseña.

Mensajes de error para credenciales incorrectas.

Dashboard de vuelos

Selección de tipo de viaje (ordinario o ida y vuelta).

Selección de destino y asiento.

Confirmación de precio (simulado).

Checklist de vuelo (core)

Lista de tareas interactivas para la preparación del vuelo.

Estado “Completado/Incompleto” actualizado dinámicamente.

Resalta la importancia de la gestión de tareas para pasajeros y tripulación.

Finalización de vuelo

Animación simple y mensaje motivador.

Resetea checklist para uso futuro.
